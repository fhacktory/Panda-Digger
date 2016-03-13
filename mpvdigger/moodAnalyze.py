#!/bin/python
# -*- coding: utf-8 -*-

from sys import argv
from tinytag import TinyTag

class MoodData:

    def __init__(self, filepath):
        self.filepath = filepath
        self.moodpath = self.filepath[:self.filepath.rfind('.')] + ".mood"
        self.kbps = 0
        self.peak_hist_1 = 0
        self.peak_hist_2 = 0
        self.peak_hist_3 = 0
        self.energy_1 = 0
        self.energy_2 = 0
        self.energy_3 = 0

        self.initCounts()
        
        self.analyze()

    def initCounts(self):
        res = {}
        for i in range(12):
            res[i] = 0
        self._countsR = res.copy()
        self._countsG = res.copy()
        self._countsB = res.copy()

    def getCountsMax(self, counts):
        maxVal = 0
        idxMax = 0
        for num,cpt in counts.iteritems():
            if cpt >= maxVal:
                maxVal = cpt
                idxMax = num
                
        return (idxMax)
    
    def analyze(self):
        with open(self.moodpath, "rb") as inputFile:
            cpt = 0
            #read mood file
            while True:
                byte = inputFile.read(3)
                if len(byte) == 3:
                    #calculate histogram
                    self._countsR[int(ord(byte[0]) / 23)] += 1
                    self._countsG[int(ord(byte[1]) / 23)] += 1
                    self._countsB[int(ord(byte[2]) / 23)] += 1
                    #calculate enery
                    self.energy_1 += pow(ord(byte[0]), 2)
                    self.energy_2 += pow(ord(byte[1]), 2)
                    self.energy_3 += pow(ord(byte[2]), 2)
                    cpt += 1
                else:
                    break

            if cpt != 0:
                #end of enery calculation
                self.energy_1 /= cpt
                self.energy_2 /= cpt
                self.energy_3 /= cpt
            
            try:
                #fetch bitrate
                tag = TinyTag.get(self.filepath)
                if tag.bitrate < 512:
                    br = int(round(tag.bitrate))
                else:
                    br = int(round(tag.bitrate/1000))
                self.kbps = br
            except OSError as ose:
                print("Error: " + str(ose))
                return (1)

            #get peak histogram
            self.peak_hist_1 = self.getCountsMax(self._countsR);
            self.peak_hist_2 = self.getCountsMax(self._countsG);
            self.peak_hist_3 = self.getCountsMax(self._countsB);

        return (0)

if __name__ == "__main__":
    if len(argv) > 1:
        data = MoodData(argv[1])
        print("Mood data of '" + data.filepath + "'")
        print("mood file: " + data.moodpath)
        print("kbps: " + str(data.kbps))
        print("energy 1: " + str(data.energy_1))
        print("energy 2: " + str(data.energy_2))
        print("energy 3: " + str(data.energy_3))
        print("peak_hist_1: " + str(data.peak_hist_1))
        print("peak_hist_2: " + str(data.peak_hist_2))
        print("peak_hist_3: " + str(data.peak_hist_3))
