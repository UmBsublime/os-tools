#!/usr/bin/env python2

import sys

from glanceclient.shell import main

from helper import parse_extra_args

if __name__ == '__main__':
    parse_extra_args()
    sys.exit(main())


