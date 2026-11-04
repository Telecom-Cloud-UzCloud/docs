#!/usr/bin/env python3
"""Checks the documentation before merge.

The table of contents in <lang>/README.md is the single source of navigation:
the site builds its menu from it. This script checks that:

  1. The table of contents follows the format described in CONTRIBUTING.md.
  2. Every page is listed in the table of contents exactly once, and every
     listed page exists.
  3. The table of contents has the same structure in all languages.
  4. All languages have the same set of pages and use the same images.
  5. Links, anchors and images in all pages resolve.
  6. Every image in images/ is used.
  7. Russian text follows the "ё" rule.

Usage: python3 scripts/check-docs.py   (exit code 1 if there are errors)
"""
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ('en', 'ru', 'uz')
IMAGES = 'images'

RE_SECTION = re.compile(r'^### (\S.*)$')
RE_GROUP = re.compile(r'^- \*\*([^*]+)\*\*$')
RE_PAGE = re.compile(r'^(  )?- \[([^\]]+)\]\(([^)\s]+\.md)\)$')
RE_LINK = re.compile(r'\]\(([^)\s]+)\)')
RE_CODE = re.compile(r'```.*?```', re.S)

errors = []


def err(msg):
    errors.append(msg)


def rel(path):
    return os.path.relpath(path, ROOT)


def slug(heading):
    """GitHub-style anchor for a heading."""
    h = heading.strip().lower()
    h = ''.join(c for c in h if c.isalnum() or c in ' -_'
                or unicodedata.category(c).startswith('L') or unicodedata.category(c) == 'Mn')
    return h.replace(' ', '-')


def anchors(path, cache={}):
    if path not in cache:
        text = RE_CODE.sub('', open(path, encoding='utf-8').read())
        cache[path] = {slug(h) for h in re.findall(r'^#+\s+(.*)$', text, re.M)}
    return cache[path]


def pages(lang):
    base = os.path.join(ROOT, lang)
    out = set()
    for d, _, files in os.walk(base):
        for f in files:
            if f.endswith('.md') and not (d == base and f == 'README.md'):
                out.add(os.path.relpath(os.path.join(d, f), base))
    return out


def parse_toc(lang):
    """Returns the navigation tree as a list of (kind, title, path) entries."""
    path = os.path.join(ROOT, lang, 'README.md')
    lines = open(path, encoding='utf-8').read().split('\n')
    start = next((i for i, l in enumerate(lines) if l.startswith('## ')), None)
    if start is None:
        err(f'{rel(path)}: no "## <Contents>" heading')
        return []
    toc, in_group, in_section = [], False, False
    for n, line in enumerate(lines[start + 1:], start + 2):
        where = f'{rel(path)}:{n}'
        if not line.strip():
            continue
        if m := RE_SECTION.match(line):
            toc.append(('section', m.group(1), None))
            in_section, in_group = True, False
        elif m := RE_GROUP.match(line):
            if not in_section:
                err(f'{where}: group outside of a "###" section')
            toc.append(('group', m.group(1), None))
            in_group = True
        elif m := RE_PAGE.match(line):
            nested = bool(m.group(1))
            if not in_section:
                err(f'{where}: page outside of a "###" section')
            if nested and not in_group:
                err(f'{where}: nested page without a group above it')
            if not nested:
                in_group = False
            toc.append(('page2' if nested else 'page', m.group(2), m.group(3)))
        else:
            err(f'{where}: line does not match the table of contents format: {line!r}')
    return toc


def check_toc(lang, toc):
    listed = {}
    for kind, title, path in toc:
        if path is None:
            continue
        if path in listed:
            err(f'{lang}/README.md: "{path}" is listed more than once')
        listed[path] = title
        if not os.path.isfile(os.path.join(ROOT, lang, path)):
            err(f'{lang}/README.md: "{path}" does not exist')
    for p in sorted(pages(lang) - set(listed)):
        err(f'{lang}/{p}: page is not listed in {lang}/README.md')


def check_links(path, used_images):
    text = RE_CODE.sub('', open(path, encoding='utf-8').read())
    base = os.path.dirname(path)
    for url in RE_LINK.findall(text):
        if url.startswith(('http://', 'https://', 'mailto:', 'tel:')):
            continue
        target, _, anchor = url.partition('#')
        full = os.path.normpath(os.path.join(base, target)) if target else path
        if not os.path.exists(full):
            err(f'{rel(path)}: broken link {url}')
            continue
        if rel(full).startswith(IMAGES + os.sep):
            used_images.add(os.path.basename(full))
        if anchor and full.endswith('.md') and anchor not in anchors(full):
            err(f'{rel(path)}: no heading for anchor {url}')


def main():
    used_images = set()
    tocs = {}
    for lang in LANGS:
        tocs[lang] = parse_toc(lang)
        check_toc(lang, tocs[lang])

    # Same navigation structure in all languages (titles are translated, paths are not)
    shape = {lang: [(k, p) for k, _, p in t] for lang, t in tocs.items()}
    for lang in LANGS[1:]:
        if shape[lang] != shape[LANGS[0]]:
            for i, (a, b) in enumerate(zip(shape[LANGS[0]], shape[lang])):
                if a != b:
                    err(f'{lang}/README.md: structure differs from {LANGS[0]}/README.md at item {i + 1}: {b} vs {a}')
                    break
            else:
                err(f'{lang}/README.md: different number of items than {LANGS[0]}/README.md')

    # Same pages and same images in every language
    page_sets = {lang: pages(lang) for lang in LANGS}
    for lang in LANGS[1:]:
        for p in sorted(page_sets[LANGS[0]] - page_sets[lang]):
            err(f'{lang}/{p}: missing (exists in {LANGS[0]})')
        for p in sorted(page_sets[lang] - page_sets[LANGS[0]]):
            err(f'{lang}/{p}: has no {LANGS[0]} version')
    for p in sorted(set.intersection(*page_sets.values())):
        imgs = {lang: re.findall(r'images/[^)\s]+', open(os.path.join(ROOT, lang, p), encoding='utf-8').read())
                for lang in LANGS}
        for lang in LANGS[1:]:
            if imgs[lang] != imgs[LANGS[0]]:
                err(f'{lang}/{p}: images differ from {LANGS[0]}/{p}')

    # Links, anchors, images
    for d, _, files in os.walk(ROOT):
        if os.sep + '.' in d or d.startswith(os.path.join(ROOT, 'node_modules')):
            continue
        for f in files:
            if f.endswith('.md'):
                check_links(os.path.join(d, f), used_images)

    # Unused images
    for img in sorted(set(os.listdir(os.path.join(ROOT, IMAGES))) - used_images):
        if not img.startswith('.'):
            err(f'{IMAGES}/{img}: not used by any page')

    # Russian: no "ё" except "всё"
    for p in sorted(page_sets['ru'] | {'README.md'}):
        text = open(os.path.join(ROOT, 'ru', p), encoding='utf-8').read()
        for n, line in enumerate(text.split('\n'), 1):
            if re.search('ё', re.sub(r'\b[Вв]сё\b', '', line)):
                err(f'ru/{p}:{n}: "ё" is not used (except "всё")')

    if errors:
        print(f'{len(errors)} problem(s) found:\n')
        print('\n'.join(f'  - {e}' for e in errors))
        return 1
    print(f'OK: {len(page_sets["en"])} pages per language, navigation and links are consistent.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
