#!/usr/bin/env python

import sys
from env import jinja_env

ctx = {
    'refs': [
        {'name': 'master',
         'commit_id': '4909c0a983f999af1187d0824d334dbfc1c8b188',
         'message': 'release 0.9.18',
         'author': 'Anton Bobrov',
         'date': 1289348574}
    ]
}


def main():
    tpl = jinja_env.get_template(sys.argv[1])
    print(tpl.render(ctx))


if __name__ == '__main__':
    main()
