"""Build the live server from native exports and the verified installed runtime."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import tomllib
import zipfile


def build(root):
    pack = tomllib.loads((root / 'pack.toml').read_text())
    assert pack['name'] == 'Astropunk'
    version = pack['version']
    runtime = root / 'build/server-installation'
    out = root / 'dist' / f'astropunk-{version}-live-server'
    archive = out.parent / (out.name + '.zip')
    client = root / 'dist' / f'astropunk-{version}-live-client.mrpack'
    server_export = root / 'dist' / f'astropunk-{version}-server.zip'
    client_export = root / 'dist' / f'astropunk-{version}-modrinth.mrpack'
    assert not out.exists() and not archive.exists()
    result = json.loads((root / 'reports/result.json').read_text())
    assert result['status'] == 'passed'
    selected = {}
    for meta in (root / 'mods').glob('*.pw.toml'):
        data = tomllib.loads(meta.read_text())
        if data.get('side', 'both') == 'client':
            continue
        name = data['filename']
        assert Path(name).name == name and name not in selected
        source = runtime / 'mods' / name
        assert source.is_file(), source
        download = data['download']
        assert hashlib.new(download['hash-format'], source.read_bytes()).hexdigest() == download['hash'], name
        selected[name] = source
    out.mkdir()
    try:
        with zipfile.ZipFile(server_export) as exported:
            assert exported.testzip() is None
            for info in exported.infolist():
                if not info.filename.startswith('overrides/') or info.is_dir():
                    continue
                rel = PurePosixPath(info.filename).relative_to('overrides')
                assert not rel.is_absolute() and '..' not in rel.parts and '\\' not in str(rel)
                assert (info.external_attr >> 16) & 0o170000 != 0o120000
                dest = out.joinpath(*rel.parts)
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(exported.read(info))
        mods = out / 'mods'
        mods.mkdir(exist_ok=True)
        for name, source in selected.items():
            shutil.copy2(source, mods / name)
        local_mods = {p.name for p in mods.glob('*.jar')} - set(selected)
        for name in local_mods:
            assert (root / 'mods' / name).read_bytes() == (runtime / 'mods' / name).read_bytes() == (mods / name).read_bytes()
        assert not any(p.is_symlink() for p in (runtime / 'libraries').rglob('*'))
        shutil.copytree(runtime / 'libraries', out / 'libraries')
        for name in ('run.sh', 'run.bat', 'user_jvm_args.txt'):
            shutil.copy2(runtime / name, out / name)
        (out / 'run.sh').chmod(0o755)
        forbidden = {'world', 'saves', 'logs', 'ops.json', 'whitelist.json', 'usercache.json', '.env', 'eula.txt', 'server.properties'}
        assert not (set(p.name for p in out.iterdir()) & forbidden)
        (out / 'UPLOAD-INSTRUCTIONS.txt').write_text((root / 'docs/hosting.md').read_text())
        files = {p.relative_to(out).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in sorted(out.rglob('*')) if p.is_file()}
        manifest = {'version': version, 'name': pack['name'], 'minecraft': pack['versions']['minecraft'],
                    'neoforge': pack['versions']['neoforge'], 'java_major': 21,
                    'server_mods': len(selected) + len(local_mods), 'world_included': False,
                    'shared_password_set': False, 'files_sha256': files}
        (out / 'payload-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
        with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=3) as z:
            for p in sorted(out.rglob('*')):
                if p.is_file():
                    z.write(p, p.relative_to(out).as_posix())
        with zipfile.ZipFile(archive) as z:
            assert z.testzip() is None
            for name, digest in files.items():
                assert hashlib.sha256(z.read(name)).hexdigest() == digest
        # Native export is authoritative. Existing same-version client is replaced
        # only after the server archive has been verified successfully.
        shutil.copy2(client_export, client)
        print(json.dumps({'folder': str(out), 'archive': str(archive), 'client': str(client),
                          'server_mods': manifest['server_mods']}, indent=2))
    except BaseException:
        shutil.rmtree(out)
        archive.unlink(missing_ok=True)
        raise


if __name__ == '__main__':
    build(Path(__file__).resolve().parents[1])
