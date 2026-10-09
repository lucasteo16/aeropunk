#!/usr/bin/env python3
"""Repeat access evidence probes. No installation or Minecraft launch."""
from pathlib import Path
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
JAVA_HOME = ROOT / 'toolchain/jdk-21.0.12.1+1'
OUTPUT = ROOT / 'build/access-investigation'
OUTPUT.mkdir(parents=True, exist_ok=True)
ENV = dict(os.environ, JAVA_HOME=str(JAVA_HOME),
           GRADLE_USER_HOME=str(ROOT / '.gradle-user-home'),
           PYTHONDONTWRITEBYTECODE='1')
ENV['PATH'] = str(JAVA_HOME / 'bin') + ':' + ENV.get('PATH', '')


def run(name, args):
    result = subprocess.run(list(map(str, args)), cwd=ROOT, env=ENV,
                            text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (OUTPUT / (name + '.log')).write_text(result.stdout)
    print(result.stdout)
    if result.returncode:
        raise SystemExit(result.returncode)


run('build', [ROOT / 'gradlew', '-I', ROOT / 'access-probe.gradle',
              'accessProbeClasspath', 'test', 'build', '--rerun-tasks', '--console=plain'])
run('negative-wiring', [sys.executable, ROOT / 'test_access_wiring.py', '--negative-control'])
run('wiring', [sys.executable, ROOT / 'test_access_wiring.py'])
run('endpoint', [sys.executable, ROOT / 'test_open_endpoint.py'])
run('artifact', [sys.executable, ROOT / 'verify_artifact.py'])
classpath = (ROOT / 'build/access-probe-classpath.txt').read_text()
classes = OUTPUT / 'classes'
classes.mkdir(exist_ok=True)
classpath += ':' + str(ROOT / 'build/classes/java/main')
run('probe-compile', [JAVA_HOME / 'bin/javac', '-proc:none', '-cp', classpath, '-d', classes,
                      ROOT / 'syntax-validation/VerifyNativeColor.java',
                      ROOT / 'syntax-validation/VerifyButtonVisibility.java'])
classpath = str(classes) + ':' + classpath
run('native-color', [JAVA_HOME / 'bin/java', '-cp', classpath, 'VerifyNativeColor'])
run('button-visibility', [JAVA_HOME / 'bin/java', '-cp', classpath,
                         'dev.astropunk.handbook.VerifyButtonVisibility'])
print('All access investigation probes passed. These do not establish runtime shortcut success.')
