import numpy as np
import os
import re
import matplotlib.pyplot as plt
import math

holes = []
solution = []
numholes = 0


def calculatePrice():
    global holes, solution
    price = 0
    maxCost = 0
    for i in range(numholes):
        edgeCost = np.linalg.norm(np.array(holes[solution[i]]) - np.array(holes[solution[(i + 1) % numholes]]))
        price = price + edgeCost
        if edgeCost > maxCost:
            maxCost = edgeCost
    return price-maxCost


def readSolution():
    global holes, solution, numholes
    fileIn = f'C:\\Users\\mn170387d\\Desktop\\in263.txt'
    fileSol = f'C:\\Users\\mn170387d\\Desktop\\solutionNN.txt'
    print("Solution file:",fileSol);

    with open(f'{fileIn}', 'r') as readerIn, open(f'{fileSol}') as readerSol:
        hole = readerIn.readline()
        sol = readerSol.readline()
        while hole != '' and sol != '':
            numholes = numholes + 1
            coords = re.findall("\-?\d+\.\d+|\-?\d+", hole)
            holes.append((float(coords[0]), float(coords[1])))

            sol = re.findall("\-?\d+\.\d+|\-?\d+", sol)
            solution.append((int(sol[0])));

            hole = readerIn.readline()
            sol = readerSol.readline()


def main():
    readSolution();

    price = calculatePrice()
    print("Minimum cost without longest edge:",price)


if __name__ == '__main__':
    main()
