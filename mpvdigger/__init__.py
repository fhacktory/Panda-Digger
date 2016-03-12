#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os
import subprocess
import sys
import time


DEVNULL = open(os.devnull, 'wb')


class Mpv(object):
    def __init__(self):
        self.playlist = []
        self.__playlist_index = -1
        self.__process = None

    def __del__(self):
        self.stop()

    def add(self, path):
        self.playlist.append(path)

    def pos(self):
        return self.__playlist_index

    def prev(self):
        self.stop()
        self.__playlist_index -= 1
        self.play(self.playlist[self.__playlist_index])

    def next(self):
        self.stop()
        self.__playlist_index += 1
        self.play(self.playlist[self.__playlist_index])

    def stop(self):
        if self.__process:
            self.__process.kill()
            self.__process = None

    def play(self, path):
        self.__process = subprocess.Popen(
            ['mpv', '-vo', 'null', path],
            stdout=DEVNULL, stderr=DEVNULL,
            close_fds=True)


def main():
    mpv = Mpv()
    for file_ in sys.argv[1:]:
        mpv.add(file_)
    for _ in xrange(5):
        mpv.next()
        print mpv.pos()
        time.sleep(5)


if __name__ == '__main__':
    main()
