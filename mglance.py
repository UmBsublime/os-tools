#!/usr/bin/env python2

import sys

from glanceclient.shell import main

from helper import get_parsed_argv

if __name__ == '__main__':
    get_parsed_argv()
    sys.exit(main())


