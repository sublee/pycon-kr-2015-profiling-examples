# -*- coding: utf-8 -*-
import gevent


def slower():
    for x in range(4):
        for y in range(10000000):
            pass
        gevent.sleep(0)


def faster():
    for x in range(2):
        for y in range(10000000):
            pass
        gevent.sleep(0)


if __name__ == '__main__':
    gevent.spawn(slower)
    gevent.spawn(faster)
    gevent.wait()
