#!/usr/bin/env python

import hashlib
import os
import sys

IGNORES = [
    ".git",
    "node_modules",
    ".cache",
    ".DS_Store",
    ".dropbox",
    "Thumbs.db",
]
SENSES = {"--unique": True, "--duplicate": False}


def main():
    if sys.argv[1] == "--unique":
        unique = True
    elif sys.argv[1] == "--duplicate":
        unique = False
    else:
        print("Unknown sense", sys.argv[1])
        sys.exit(1)

    roots = sys.argv[2:]
    if not roots:
        roots = [os.curdir]

    found = {}
    count = 0
    for r in roots:
        count = find(r, found, count)

    report(unique, found)


def find(root, found, count):
    for (dirpath, dirnames, filenames) in os.walk(root):
        ignore = False
        for i in IGNORES:
            if i in dirpath:
                ignore = True
        if ignore:
            continue
        count += 1
        if (count % 10) == 0:
            print(count, file=sys.stderr)
        for f in filenames:
            path = os.path.join(dirpath, f)
            if not os.path.isfile(path):
                continue
            with open(path, "r") as reader:
                data = reader.read()
                digest = hashlib.md5(data).digest()
                if digest not in found:
                    found[digest] = set()
                found[digest].add(path)
    return count


def report(unique, found):
    for digest in found:
        paths = found[digest]
        if unique and (len(paths) == 1):
            print(paths.pop())
        elif (not unique) and (len(paths) > 1):
            print(", ".join(sorted(paths)))


if __name__ == "__main__":
    main()
