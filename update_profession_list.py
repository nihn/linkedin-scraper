#!/usr/bin/env python

from os import remove
from subprocess import check_call

check_call(['docker-compose', 'run', '--entrypoint', 'scrapy',
            'crawler', 'crawl', 'career_update', '-o', 'tmp.csv'])

try:
    with open('tmp.csv') as f:
        lines = set(line.lower().strip() for line in f.readlines()[1:])

    # Add common corporate titles
    lines |= {'CEO', 'CTO', 'CAO', 'CBO', 'CFO'}

    with open('data/professions_list.txt', 'w+') as f:
        f.write('\n'.join(line for line in sorted(lines)
                          if not line.endswith('ing')))
finally:
    remove('tmp.csv')
