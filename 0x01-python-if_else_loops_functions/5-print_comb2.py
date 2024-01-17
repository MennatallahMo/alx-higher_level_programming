#!/usr/bin/python3
for no in range(0, 100):
    if no != 99:
        print("{} {} {}".format(str(no).zfill(2), ','," "),end="")
    else:
        print("{} {}".format(str(no).zfill(2)," "),end="\n")
