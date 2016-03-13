#!/bin/python
# -*- coding: utf-8 -*-

from sys import argv

def usage():
    print("Usage: " + argv[0] + " output.csv file1.mood [file2.mood ...]")

def initCounts():
    res = {}
    for i in range(12):
        res[i] = 0
    return (res)

def getCountsMax(counts):
    maxVal = 0
    idxMax = 0
    for num,cpt in counts.iteritems():
        if cpt >= maxVal:
            maxVal = cpt
            idxMax = num

    return (idxMax)

def writeHist(hist, output):
    for idx,cpt in hist.iteritems():
        output.write(str(cpt) + ";")
    output.write("\n")

def genMoodHist(fileName, inputFile, outputFile, localOutput):
    countsR = initCounts()
    countsG = initCounts()
    countsB = initCounts()

    while True:
        byte = inputFile.read(3)
        if len(byte) == 3:
            countsR[int(ord(byte[0]) / 23)] += 1
            countsG[int(ord(byte[1]) / 23)] += 1
            countsB[int(ord(byte[2]) / 23)] += 1
        else:
            break

    for binIdx in range(12):
        xMin = binIdx * 23
        xMax = xMin + 22
        localOutput.write(str(xMin) + "-" + str(xMax) + ";")
    localOutput.write("\n")

    writeHist(countsR, localOutput)
    writeHist(countsG, localOutput)
    writeHist(countsB, localOutput)

    outputFile.write(fileName + ";" +
                     str(getCountsMax(countsR)) + ";" +
                     str(getCountsMax(countsG)) + ";" +
                     str(getCountsMax(countsB)) + "\n")

    return (0)

def moodHist():
    if len(argv) <= 2:
        usage()
        return (1)

    outputPath = argv[1]
    
    with open(outputPath, "w+") as outputFile:
        for filepath in argv[2:]:
            ext = filepath[-5:]
            if ext == ".mood":
                with open(filepath, "rb") as inputFile:
                    with open(filepath[:-5] + ".hist.csv", "w+") as localOutput:
                        ret = genMoodHist(filepath, inputFile, outputFile, localOutput)
                        if ret != 0:
                            return ret
            else:
                print("'" + filepath + "': not a mood file")
    
    return (0)
        

    
if __name__ == "__main__":
    exit(moodHist())
