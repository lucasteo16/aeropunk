"""Restore a checked historical result for historical preservation assertions.

Later approved prose must not invalidate an earlier image-only contract. Verify
the later revision's exact before and after hashes before restoring it, so this
does not exempt those topics from change detection.
"""
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def topic_digest(locales):
    return hashlib.sha256(json.dumps(locales, ensure_ascii=False,
                                    sort_keys=True).encode()).hexdigest()


def refurbished_topics():
    """Topics a later refurbishment batch owns, with its own stricter test."""
    path = ROOT / 'docs/handbook-refurbish-scope.json'
    if not path.exists():
        return set()
    batches = json.loads(path.read_text())['batches']
    return {topic for batch in batches.values() for topic in batch['topics']}


def before_development_update(content, include_mars_retirement=False):
    revision = json.loads((ROOT / 'docs/handbook-development-update.json').read_text())
    later = refurbished_topics()
    before = json.loads(subprocess.check_output([
        'git', 'show', revision['guide_parent_commit'] + ':docs/handbook-content.json'
    ], cwd=ROOT, text=True))
    restored = dict(content)
    for topic, hashes in revision['topic_sha256'].items():
        assert topic_digest(before[topic]) == hashes['before'], ('Historical source mismatch', topic)
        if topic in later:
            continue
        assert topic_digest(content[topic]) == hashes['after'], ('Unapproved later edit', topic)
        restored[topic] = before[topic]
    if include_mars_retirement:
        retirement = revision['prior_mars_retirement']
        original = json.loads(subprocess.check_output([
            'git', 'show', retirement['parent_commit'] + ':docs/handbook-content.json'
        ], cwd=ROOT, text=True))
        for topic, hashes in retirement['topic_sha256'].items():
            assert topic_digest(original[topic]) == hashes['before'], ('Pre-retirement source mismatch', topic)
            if topic in later:
                continue
            assert topic_digest(restored[topic]) == hashes['after'], ('Retirement source mismatch', topic)
            restored[topic] = original[topic]
    return restored