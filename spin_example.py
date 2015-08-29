# -*- coding: utf-8 -*-
import time


def spin(sec):
    t = time.time()
    while time.time() - t < sec:
        pass


def spin5():
    spin(5)


if __name__ == '__main__':
    spin5()
