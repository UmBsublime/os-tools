#!/usr/bin/env python2

import sys

from neutronclient.shell import main

from helper import parse_extra_args

if __name__ == '__main__':
    parse_extra_args()
    sys.argv.pop(0)
    sys.exit(main(sys.argv))


