#!/usr/bin/env python

import os
import sys

from os.path import dirname, abspath, join

sys.path.insert(0, dirname(dirname(abspath(__file__))))

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resultsrecorder.settings')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
