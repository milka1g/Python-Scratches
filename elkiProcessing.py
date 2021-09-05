import numpy as np
import os
import re
from pathlib import Path


def readFiles():
    files = []
    directory = f'C:\\Users\\mn170387d\\Desktop\\manual'
    for filename in os.listdir(directory):
        if 'cluster' in filename:
            fullname = os.path.join(directory, filename)
            files.append(fullname)
        else:
            continue
    return files


def processFile(file):
    basename = os.path.basename(file)

    numHoles = 0
    with open(f'{file}', 'r') as reader:
        for line in reader:
            if 'ID' in line:
                numHoles = numHoles + 1


    fprocessed = open(f'C:\\Users\\mn170387d\\Desktop\\manual\\{basename}', "w+")
    fprocessed.write(str(numHoles) + '\n')

    fmeans = open(f'C:\\Users\\mn170387d\\Desktop\\manual\\cluster means.txt', "a")
    pathMeans = Path(f'C:\\Users\\mn170387d\\Desktop\\manual\\cluster means.txt')
    if pathMeans.stat().st_size == 0:
        fmeans.write("16\n")

    with open(f'{file}', 'r') as reader:
        for line in reader:
            if 'Cluster Mean' in line:
                coords = re.findall("\-?\d+\.\d+", line)
                clusterMean = str(round(float(coords[0]),4)) + " " + str(round(float(coords[1]),4))
                fmeans.write(clusterMean + '\n')
            if 'ID' in line:
                coords = re.findall("\-?\d+\.\d+", line)
                coordHole = coords[0] + " " + coords[1]
                fprocessed.write(coordHole + '\n')
        fprocessed.write("cluster mean: " + clusterMean)
        fprocessed.close()
    fmeans.close()


def main():
    files = readFiles()
    for file in files:
        processFile(file)


if __name__ == '__main__':
    main()
