# Panda-Digger
Playlist intelligente sur base de moodbar(s)

A long time ago in a galaxy far far away, Gavin Wood and Simon O'Keefe from the Univerity of York invented the moodbar. It was designed to facilitate navigation on music.

It was first designed for [Amarok](https://amarok.kde.org/en) and it was later included in many other music players (like [Exaile](http://www.exaile.org/), [XMMS2](https://xmms2.org/wiki/Main_Page) and [clementine](https://www.clementine-player.org/)).

## Mood-analyzer
The .mood files contain the magnitude of the spectral analysis split into 3 channels (R, G, B). Our feature vector is composed by the spectral energy in the 3 sub-bands, the histogram peaks for the 3 channels and kbps metadata.
In songs, we can identify 12 musical notes. As a result, our histogram contains 12 bins and for each channel the peak is extracted. 
Manual labelling was done on more than 250 songs. We chose 3 mood classes (sad, happy, excited). 
Supervised learning was performed using decision trees. Confusion matrix yeld 40% succes rate for 265 music samples.

A particular challenge was the labelling process as some rythms are hard to be associated with the identified moods. 

## Dependencies

* `pip install django`
* `pip install tinytag`

## Web interface

* Run Django server: `python webdigger/manage.py runserver 0.0.0.0:8000`

## Tools

* Generating a .mood file from a .mp3: `moodGen.sh file1.mp3 [file2.mp3 ...]`
* Generating a .csv file from a .mood: `moodCSV.py file1.mood [file2.mood ...]` (requires python 2.7)
* Generating a .bmp moodbar from a .mood: `moodBMP.py imageHeight file1.mood [file2.mood ...]` (requires python 2.7)

