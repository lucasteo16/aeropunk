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
    food = ROOT / 'docs/food-chapter-final-review.json'
    if food.exists():
        # Pair a restored historical body with its historical ownership scope.
        commit = json.loads(food.read_text())['development_base']
        scope = subprocess.check_output([
            'git', 'show', commit + ':docs/handbook-refurbish-scope.json'
        ], cwd=ROOT, text=True)
    else:
        scope = path.read_text()
    batches = json.loads(scope)['batches']
    return {topic for batch in batches.values() for topic in batch['topics']}


def before_food_finalization(content):
    """Restore the exact approved Food revision, not an exempted topic list."""
    path = ROOT / 'docs/food-chapter-final-review.json'
    if not path.exists():
        return dict(content)
    revision = json.loads(path.read_text())
    commit = revision['development_base']
    assert len(commit) == 40 and all(c in '0123456789abcdef' for c in commit)
    before = json.loads(subprocess.check_output([
        'git', 'show', commit + ':docs/handbook-content.json'
    ], cwd=ROOT, text=True))
    hashes = revision['source_sha256']
    assert topic_digest(before) == hashes['before'], 'Food historical source mismatch'
    actual = topic_digest(content)
    if actual == hashes['before']:
        return before
    assert actual == hashes['after'], 'Unapproved edit after Food finalization'
    return before


def before_development_update(content, include_mars_retirement=False):
    content = before_food_finalization(content)
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