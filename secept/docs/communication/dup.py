#!/usr/bin/env python

## Add a docstring describing the program.

import hashlib
import os
import sys

IGNORES = [ ## Use a set instead of a list for lookup tables.
    ".git",
    "node_modules",
    ".cache",
    ".DS_Store",
    ".dropbox",
    "Thumbs.db",
]

SENSES = { ## not used anywhere - delete
    "--unique": True,
    "--duplicate": False
}


def main():
    ## add a docstring describing this function
    ## use the argparse library to handle options
    ## put option handling in its own function
    if sys.argv[1] == "--unique":
        unique = True
    elif sys.argv[1] == "--duplicate":
        unique = False
    else:
        ## print error messages to sys.stderr
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
    ## add a docstring describing this function
    for (dirpath, dirnames, filenames) in os.walk(root):
        ignore = False
        ## use any() instead of a loop for this check
        for i in IGNORES:
            if i in dirpath:
                ignore = True
        if ignore:
            continue
        count += 1
        ## 10 is a magic number: define a constant
        ## provide a command-line option to control reporting
        if (count % 10) == 0:
            print(count, file=sys.stderr)
        for f in filenames:
            path = os.path.join(dirpath, f)
            if not os.path.isfile(path):
                continue
            ## use "rb" to read files in binary  mode
            with open(path, "r") as reader:
                data = reader.read()
                digest = hashlib.md5(data).digest()
                if digest not in found:
                    found[digest] = set()
                found[digest].add(path)
    return count


def report(unique, found):
    ## add a docstring describing this function
    for digest in found:
        paths = found[digest]
        if unique and (len(paths) == 1):
            ## why paths.pop() ?
            print(paths.pop())
        elif (not unique) and (len(paths) > 1):
            print(", ".join(sorted(paths)))


if __name__ == "__main__":
    main()
