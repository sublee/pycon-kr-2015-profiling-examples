# -*- coding: utf-8 -*-
from gevent import getcurrent
import yappi


@yappi.set_context_id_callback
def current_greenlet_id():
    return id(getcurrent())


@yappi.set_context_name_callback
def current_greenlet_name():
    return type(getcurrent()).__name__


if __name__ == '__main__':
    yappi.main()
