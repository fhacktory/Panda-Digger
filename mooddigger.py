#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def usage():
    print 'George is mad at you! Return to JavaScript!'


def launch_webdigger():
    sys.path.extend(('webdigger', '.'))
    import manage
    argv = [sys.argv[0], 'runserver', '0.0.0.0:8000']
    manage.main(argv)


def main():
    if len(sys.argv) != 2:
        usage()
    else:
        sys.path.extend(('webdigger', '.'))
        import mpvdigger
        mpvdigger.mpv.set_library_root_path(sys.argv[1])
        launch_webdigger()


if __name__ == '__main__':
    main()
