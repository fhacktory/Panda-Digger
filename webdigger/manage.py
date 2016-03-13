#!/usr/bin/env python
import os
import sys


def main(argv):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pandadigger.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(argv)


if __name__ == "__main__":
    main(sys.argv)
