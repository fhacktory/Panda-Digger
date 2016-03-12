# Panda-Digger
Playlist intelligente sur base de moodbar(s)

A long time ago in a galaxy far far away, Gavin Wood and Simon O'Keefe from the Univerity of York invented the moodbar. It was designed to facilitate navigation on music.

It was first designed for [Amarok](https://amarok.kde.org/en) and it was later included in many other music players (like [Exaile](http://www.exaile.org/), [XMMS2](https://xmms2.org/wiki/Main_Page) and [clementine](https://www.clementine-player.org/)).

## Web interface

* Run Django server: `python webdigger/manage.py runserver 0.0.0.0:8000`

## Tools

* Generating a .mood file from a .mp3: `moodGen.sh file1.mp3 [file2.mp3 ...]`
* Generating a .csv file from a .mood: `moodCSV.py file1.mood [file2.mood ...]` (requires python 2.7)
* Generating a .bmp moodbar from a .mood: `moodBMP.py imageHeight file1.mood [file2.mood ...]` (requires python 2.7)

