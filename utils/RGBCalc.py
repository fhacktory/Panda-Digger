import sys

table = []
total = [0,0,0]
for arg in sys.argv[1:]:
    ct = 0;
    with open(sys.argv[1], 'r') as fd:
        for line in fd:
            table.append(line.strip().split(";"))
            ct += 1;
    for i in range(0,3):
        subtotal = float(0)
        for rgb in table:
            subtotal += pow(int(rgb[i]), 2)
        subtotal /= ct
        print("{0}: {1} ({2})".format(i, subtotal, arg))
        print("---")
        total[i] += subtotal 
for i in range(0, 3):
    print("-- {0}: {1}".format(i, total[i]))
