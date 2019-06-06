import os
import sys
import json
from sys import exit

try:
    with open('config.json') as config:
        cfg = json.load(config)
except:
    print("You must create a config.json file. An example file is provided: example-config.json")
    print("Edit the file and change the name to config.json")
    exit(0)


def main():
    inputdir = cfg["historyDir"]
    outputloc = cfg["allHistory"]
    out = open(outputloc, "wt")
    flip = 0
    first = 0

    for filename in os.listdir(inputdir):
        with open(inputdir + filename) as f:
            print("processing " + inputdir + filename)
            if flip == 0:
                flip += 1
            else:
                f.readline()

            for line in f:
                if first == 0:
                    out.write("symbol," + line)
                    first = 1
                else:
                    sym = ((filename.split("."))[0]).replace("-", ".")
                    out.write(sym + "," + line)
    out.close()


main()
