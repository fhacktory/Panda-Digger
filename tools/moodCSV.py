#!/bin/python
# -*- coding: utf-8 -*-

from sys import argv


#Prints the command syntax
def usage():
    print("Usage: " + argv[0] + " file1.mood [file2.mood ...]")


#Generates a csv file for a given mood file
def generateCSV(inputPath, outputPath):
    with open(inputPath, "rb") as inputFile:
        with open(outputPath, "w") as outputFile:
            while True:
                byte = inputFile.read(3)
                if len(byte) == 3:
                    outputFile.write(str(byte[0]) + ";" + str(byte[1]) + ";" + str(byte[2]) + "\n")
                else:
                    break

#Generates a csv file for each mood file given in argument
def moodCSV():
    if len(argv) <= 1:
        usage()
        return (1)
    
    for arg in argv[1:]:
        ext = arg[-5:]
        if ext == ".mood":
            ret = generateCSV(arg, arg[:-5] + ".csv")
            
            if ret != 0:
                return (ret)
        else:
            print(arg + ": not a mood file")
            return (1)
    
    return (0)

if __name__ == "__main__":
    exit(moodCSV())
