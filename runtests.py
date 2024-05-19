#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import pytest

if __name__ == '__main__':
    sys.path.insert(0, 'tests')
    if os.environ.get('POSTGRESQL', False):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'immunity22.postgresql_settings')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'immunity22.settings')
    from django.core.management import execute_from_command_line

    args = sys.argv
    args.insert(1, 'test')

    if not os.environ.get('SAMPLE_APP', False):
        args.insert(2, 'immunity_controller')
    else:
        args.insert(2, 'immunity22')

    if os.environ.get('POSTGRESQL', False):
        args.extend(['--tag', 'db_tests'])
        args.extend(['--tag', 'selenium_tests'])
    else:
        args.extend(['--exclude-tag', 'selenium_tests'])

    execute_from_command_line(args)

    if not os.environ.get('SAMPLE_APP', False):
        app_dir = 'immunity_controller/'
    else:
        app_dir = 'tests/immunity22/'

    sys.exit(pytest.main([app_dir]))
