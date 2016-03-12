from tinytag import TinyTag
import sys

for arg in sys.argv[1:]:
    try:
        tag = TinyTag.get(arg)
        if tag.bitrate < 512:
            br = int(round(tag.bitrate))
        else:
            br = int(round(tag.bitrate/1000))
        print("{0}: {1} kBits/s".format(arg, br))
    except OSError as ose:
        print("Error: " + str(ose))
