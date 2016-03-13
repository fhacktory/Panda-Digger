#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple
import glob
import os
import random
import subprocess
import sys
import threading
import time

from tinytag import TinyTag


DEVNULL = open(os.devnull, 'wb')


Entry = namedtuple('Entry', ('path', 'artist', 'album', 'title', 'duration'))


class Mpv(object):
    def __init__(self):
        self.playlist = []
        self.__playlist_index = -1
        self.__process = None
        self.__library = []
        self.__lock = threading.Lock()

    def __del__(self):
        self.stop()

    def set_library_root_path(self, root):
        root = os.path.abspath(root)
        library = []
        for path, _, files in os.walk(root):
            if not files:
                continue

            for file_ in files:
                if file_.endswith('.mp3'):
                    library.append(os.path.join(path, file_))

        print 'found {} titles'.format(len(library))
        self.__library = library
        while not self.playlist:
            self.add_random()

    def add(self, path):
        try:
            tag = TinyTag.get(path)
        except:
            artiste = 'Pas'
            album = 'de'
            title = 'chocolat'
            duration = '!'
        else:
            artist = tag.artist
            album = tag.album
            title = tag.title
            duration = int(tag.duration)
            duration = '{:02}:{:02}'.format(duration / 60, duration % 60)
        entry = Entry(path, artist, album, title, duration)
        self.playlist.append(entry)

    def add_random(self):
        with self.__lock:
            choice = random.choice(self.__library)
            self.add(choice)

    @property
    def pos(self):
        return self.__playlist_index

    def goto(self, index):
        self.stop()
        self.__playlist_index = index
        self.play(self.__playlist_index)

    def prev(self):
        self.goto(self.__playlist_index - 1)

    def next(self):
        self.goto(self.__playlist_index + 1)

    def stop(self):
        if self.__process:
            self.__process.kill()
            self.__process = None
            self.__playlist_index = -1

    def play(self, index):
        entry = self.playlist[index]
        self.__process = subprocess.Popen(
            ['mpv', '-vo', 'null', entry.path],
            stdout=DEVNULL, stderr=DEVNULL,
            close_fds=True)
        if index == len(self.playlist) - 1:
            threading.Thread(target=self.add_random).start()


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
else:
    mpv = Mpv()
