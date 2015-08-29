# -*- coding: utf-8 -*-
from flask import Flask


app = Flask(__name__)


@app.route('/<int:n>')
def fac(n):
    r = 1
    for x in range(2, n + 1):
        r *= x
    return str(r)


if __name__ == '__main__':
    app.run(port=8080)
