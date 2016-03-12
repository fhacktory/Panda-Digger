#!/bin/python
# -*- coding: utf-8 -*-

import Image
import struct
from sys import argv
from os.path import getsize
from os import error

#CLI syntax
def usage():
    print("Usage: " + argv[0] + " height file1 [file2 ...]")

#Get the size of a file
def getFileSize(path):
    res = 0

    try:
        res = getsize(path)
    except OSError as e:
        print("'" + path + "': no such file")
    return (res)

#BMP generation function
def genBMP(width, height, inputFile, outputPath):
    img = Image.new("RGB", (width,height), "black")
    pixels = img.load()

    x = 0
    while True:
        byte = inputFile.read(3)
        if len(byte) == 3:
            for i in range(height):
                r = ord(byte[0])
                g = ord(byte[1])
                b = ord(byte[2])
                pixels[x,i] = (r, g, b)
        else:
            break
        x += 1

    ret = 0
    try:
        img.save(outputPath, "BMP")
    except:
        print("Error while generating moodbar '" + outputPath + "'")
        ret = 1
    
    return (ret)

#Main function
#Syntax check & arg parsing
def moodBMP():
    if len(argv) < 3:
        usage()
        return (1)

    height = int(argv[1])
    if height >= 1024:
        height = 1024
    elif height < 0:
        height = 1

    print("Generating " + str(height) + "px high moodbar(s)")

    for filepath in argv[2:]:
        width = getFileSize(filepath)
        if width > 3:
            width /= 3
            with open(filepath, "rb") as inputFile:
                ret = genBMP(width, height, inputFile, filepath[:-5] + ".bmp")
                if ret != 0:
                    break

    return (0)

if __name__ == "__main__":
    exit(moodBMP())
