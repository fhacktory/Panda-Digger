#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple
import glob
import os
import subprocess
import sys
import time

from tinytag import TinyTag


DEVNULL = open(os.devnull, 'wb')


Entry = namedtuple('Entry', ('path', 'artist', 'album', 'title', 'duration'))


class Mpv(object):
    def __init__(self):
        self.playlist = []
        self.__playlist_index = -1
        self.__process = None

    def __del__(self):
        self.stop()

    def add(self, path):
        tag = TinyTag.get(path)
        artist = tag.artist or 'No arsist'
        album = tag.album or 'No album'
        title = tag.title or 'No title'
        duration = int(tag.duration)
        duration = '{:02}:{:02}'.format(duration / 60, duration % 60)
        entry = Entry(path, artist, album, title, duration)
        self.playlist.append(entry)

    @property
    def pos(self):
        return self.__playlist_index

    def goto(self, index):
        self.stop()
        self.__playlist_index = index
        entry = self.playlist[self.__playlist_index]
        self.play(entry.path)

    def prev(self):
        self.goto(self.__playlist_index - 1)

    def next(self):
        self.goto(self.__playlist_index + 1)

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
