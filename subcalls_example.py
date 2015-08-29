# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import timeit


def f():
    pass


def shallow(n):
    for x in range(n):
        f()


def deep(n):
    if n != 0:
        deep(n - 1)


if __name__ == '__main__':
    try:
        func_name = sys.argv[1]
    except IndexError:
        print('Usage: python subcalls_example.py shallow|deep [100]')
        raise SystemExit(1)
    try:
        n = int(sys.argv[2])
    except IndexError:
        n = 100
    timeit.main(['-s', 'from subcalls_example '
                 'import %s as f' % func_name,
                 'f(%d)' % n])
