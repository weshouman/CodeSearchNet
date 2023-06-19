#!/usr/bin/env python
"""
Usage:
    download_dataset.py DESTINATION_DIR

Options:
    -h --help   Show this screen.
"""

import os
from subprocess import call

from docopt import docopt


if __name__ == '__main__':
    args = docopt(__doc__)

    destination_dir = os.path.abspath(args['DESTINATION_DIR'])
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    os.chdir(destination_dir)

    for language in ('python', 'javascript', 'java', 'ruby', 'php', 'go'):
        lang_dir = os.path.join(destination_dir, language)
        if os.path.exists(lang_dir):
            print(f"{lang_dir} was found, skipping downloading {language}.zip")
        else:
            call(['wget', 'https://zenodo.org/record/7857872/files/{}.zip'.format(language), '-P', destination_dir, '-O', '{}.zip'.format(language)])
            call(['unzip', '{}.zip'.format(language)])
            call(['rm', '{}.zip'.format(language)])

