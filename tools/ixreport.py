#!/usr/bin/env python3
"""Report on the grid index: counts, and groups of index terms that are probably
the same thing spelled differently (case, plural, punctuation, () on functions).
Usage: python3 tools/ixreport.py main.idx [--all]
Fix variants by adding \\ixalias{variant}{canonical} lines to index_aliases.tex."""
import re, sys, collections

ENTRY = re.compile(r'^\\indexentry\{(.*)\}\{(\d+)\}\s*$')


def split_entry(s):
    """split key@display|encap honouring makeindex's " quoting."""
    parts, cur, i = [], '', 0
    key = disp = enc = None
    out = {'@': None, '|': None}
    buf, field = '', 'key'
    while i < len(s):
        c = s[i]
        if c == '"' and i + 1 < len(s):
            buf += s[i + 1]; i += 2; continue
        if c == '@' and field == 'key':
            key, buf, field = buf, '', 'disp'; i += 1; continue
        if c == '|' and field in ('key', 'disp'):
            if field == 'key':
                key = buf
                disp = buf
            else:
                disp = buf
            buf, field = '', 'enc'; i += 1; continue
        buf += c; i += 1
    if field == 'enc':
        enc = buf
    elif field == 'disp':
        disp = buf
    else:
        key = disp = buf
    return key, disp, enc


def norm(display):
    d = display.replace('\\ixcodefmt', '')
    d = re.sub(r'\\[a-zA-Z]+', '', d).replace('\\', '')
    d = d.lower()
    d = re.sub(r'\(\)', '', d)
    d = re.sub(r'[^a-z0-9%>|]+', ' ', d).strip()
    words = [w[:-1] if len(w) > 3 and w.endswith('s') and not w.endswith('ss') else w for w in d.split()]
    return ' '.join(words)


def main():
    path = sys.argv[1]
    show_all = '--all' in sys.argv
    terms = collections.defaultdict(lambda: collections.Counter())
    total = 0
    enc_count = collections.Counter()
    for line in open(path, encoding='utf-8', errors='replace'):
        m = ENTRY.match(line.strip())
        if not m:
            continue
        key, disp, enc = split_entry(m.group(1))
        if enc and enc.startswith('see'):
            continue
        total += 1
        enc_count[enc] += 1
        terms[disp][enc] += 1
    print(f'locations written: {total}  (distilled {enc_count["ixD"]}, raw {enc_count["ixR"]})')
    print(f'distinct index terms: {len(terms)}')
    groups = collections.defaultdict(list)
    for disp in terms:
        groups[norm(disp)].append(disp)
    print('\n== probable variants (same normalised form, different spelling):')
    for n, ds in sorted(groups.items()):
        if len(ds) > 1:
            ds = sorted(ds, key=lambda d: -sum(terms[d].values()))
            print('  ' + '  |  '.join(f'{d} ({sum(terms[d].values())})' for d in ds))
    only_raw = [d for d in terms if terms[d]['ixD'] == 0]
    only_dist = [d for d in terms if terms[d]['ixR'] == 0]
    print(f'\n== terms only in raw part: {len(only_raw)};  only in distilled part: {len(only_dist)}')
    if show_all:
        for d in sorted(terms, key=lambda d: norm(d)):
            print(f'  {d}: D={terms[d]["ixD"]} R={terms[d]["ixR"]}')


if __name__ == '__main__':
    main()
