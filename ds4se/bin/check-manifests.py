#!/usr/bin/env python

'''Check that all manifests are up to date.'''

import os
import glob
import fnmatch
import yaml
import itertools

import utils

IGNORE = ['*/*~', '*/*.py', '*/*.svg', '*/MANIFEST.md', '*/index.md']


def check_manifests(options):
    '''Main driver.'''
    for where in args.folders:
        expected = get_expected(where)
        if expected is None:
            continue
        actual = get_actual(where)
        report('missing from manifest', actual - expected)
        report('missing from directory', expected - actual)


def get_expected(where):
    filename = os.path.join(where, 'MANIFEST.md')
    manifest = utils.read_yaml(filename)
    assert all([('path' in x) for x in manifest]), \
        f'{where}: Not all manifest entries contain path'
    expected = [x['path'] for x in manifest]
    assert len(expected) == len(set(expected)), \
        'Redundant paths in manifest'
    expected = set([os.path.join(where, x) for x in expected])
    return expected


def get_actual(where):
    actual = glob.glob(os.path.join(where, '**/*.*'), recursive=True)
    actual = set([x for x in actual if keep(x)])
    return actual


def keep(filename):
    return not any([fnmatch.fnmatch(filename, pat) for pat in IGNORE])


def report(title, values):
    if values:
        print(title)
        for v in sorted(values):
            print(f'- {v}')


if __name__ == '__main__':
    options = utils.get_options(
        ['--folders', True, 'List of folders']
    )
    check_manifests(options)
