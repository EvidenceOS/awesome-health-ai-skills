#!/usr/bin/env python3
"""Validate all SKILL.md files in the repository.

Checks:
1. Required frontmatter fields present
2. Required content sections present
3. Category matches directory structure
4. Prerequisites reference existing skills
5. Skills index matches filesystem
"""

import os
import sys
import json
import re
from pathlib import Path

REQUIRED_FRONTMATTER = [
    "name", "description", "category", "raigh_tier",
    "difficulty", "estimated_time", "prerequisites", "tags", "version"
]

REQUIRED_SECTIONS = [
    "## Purpose",
    "## Learning Objectives",
    "## Steps",
    "## Artifacts",
    "## Assessment Criteria",
    "## Common Mistakes",
    "## Related Skills",
    "## References"
]

VALID_CATEGORIES = [
    "pre-mooc",
    "digital-health-foundations",
    "ai-evaluation",
    "clinical-ai",
    "dpi-architecture",
    "regulatory",
    "institutional-intelligence"
]

VALID_TIERS = ["MOOC", "tier-1", "tier-2", "tier-3"]
VALID_DIFFICULTIES = ["beginner", "intermediate", "advanced"]


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from SKILL.md content."""
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}

    frontmatter = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, _, value = line.partition(':')
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if value.startswith('['):
                # Simple array parsing
                value = [v.strip().strip('"').strip("'") for v in value[1:-1].split(',') if v.strip()]
            frontmatter[key] = value
    return frontmatter


def validate_skill(skill_path: Path, all_skill_names: set) -> list:
    """Validate a single SKILL.md file. Returns list of errors."""
    errors = []
    content = skill_path.read_text(encoding='utf-8')

    # Check frontmatter
    fm = parse_frontmatter(content)
    if not fm:
        errors.append(f"  Missing or invalid frontmatter")
        return errors

    for field in REQUIRED_FRONTMATTER:
        if field not in fm:
            errors.append(f"  Missing frontmatter field: {field}")

    # Validate category
    if 'category' in fm and fm['category'] not in VALID_CATEGORIES:
        errors.append(f"  Invalid category: {fm['category']}")

    # Validate tier
    if 'raigh_tier' in fm and fm['raigh_tier'] not in VALID_TIERS:
        errors.append(f"  Invalid raigh_tier: {fm['raigh_tier']}")

    # Validate difficulty
    if 'difficulty' in fm and fm['difficulty'] not in VALID_DIFFICULTIES:
        errors.append(f"  Invalid difficulty: {fm['difficulty']}")

    # Check category matches directory
    if 'category' in fm:
        expected_dir = fm['category']
        actual_dir = skill_path.parent.parent.name
        if expected_dir != actual_dir:
            errors.append(f"  Category mismatch: frontmatter says '{expected_dir}', file is in '{actual_dir}'")

    # Check name matches directory
    if 'name' in fm:
        expected_name = fm['name']
        actual_name = skill_path.parent.name
        if expected_name != actual_name:
            errors.append(f"  Name mismatch: frontmatter says '{expected_name}', directory is '{actual_name}'")

    # Check prerequisites reference existing skills
    if 'prerequisites' in fm and isinstance(fm['prerequisites'], list):
        for prereq in fm['prerequisites']:
            if prereq and prereq not in all_skill_names:
                errors.append(f"  Unknown prerequisite: {prereq}")

    # Check required sections
    for section in REQUIRED_SECTIONS:
        if section not in content:
            errors.append(f"  Missing section: {section}")

    return errors


def validate_index(skills_dir: Path, index_path: Path) -> list:
    """Validate skills_index.json matches filesystem."""
    errors = []

    if not index_path.exists():
        errors.append("skills_index.json not found")
        return errors

    with open(index_path, encoding='utf-8') as f:
        index = json.load(f)

    # Get all skills from filesystem
    fs_skills = set()
    for skill_md in skills_dir.rglob('SKILL.md'):
        fs_skills.add(skill_md.parent.name)

    # Get all skills from index
    idx_skills = set(s['name'] for s in index['skills'])

    # Check for mismatches
    missing_from_index = fs_skills - idx_skills
    missing_from_fs = idx_skills - fs_skills

    for name in missing_from_index:
        errors.append(f"Skill '{name}' exists on filesystem but not in index")
    for name in missing_from_fs:
        errors.append(f"Skill '{name}' in index but not on filesystem")

    return errors


def main():
    repo_root = Path(__file__).parent.parent
    skills_dir = repo_root / 'skills'
    index_path = repo_root / 'data' / 'skills_index.json'

    if not skills_dir.exists():
        print("ERROR: skills/ directory not found")
        sys.exit(1)

    # Collect all skill names
    all_skill_names = set()
    skill_files = list(skills_dir.rglob('SKILL.md'))
    for skill_path in skill_files:
        all_skill_names.add(skill_path.parent.name)

    print(f"Found {len(skill_files)} skills across {len(set(p.parent.parent.name for p in skill_files))} categories\n")

    total_errors = 0

    # Validate each skill
    for skill_path in sorted(skill_files):
        rel_path = skill_path.relative_to(repo_root)
        errors = validate_skill(skill_path, all_skill_names)
        if errors:
            print(f"FAIL: {rel_path}")
            for e in errors:
                print(e)
            total_errors += len(errors)
        else:
            print(f"  OK: {rel_path}")

    # Validate index
    print(f"\nValidating skills_index.json...")
    idx_errors = validate_index(skills_dir, index_path)
    if idx_errors:
        for e in idx_errors:
            print(f"  FAIL: {e}")
        total_errors += len(idx_errors)
    else:
        print("  OK: Index matches filesystem")

    print(f"\n{'='*50}")
    if total_errors == 0:
        print(f"ALL CHECKS PASSED ({len(skill_files)} skills validated)")
        sys.exit(0)
    else:
        print(f"FAILED: {total_errors} errors found")
        sys.exit(1)


if __name__ == '__main__':
    main()
