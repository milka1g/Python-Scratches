import numpy as np
import os
import re
import matplotlib.pyplot as plt
import math

numholes = 0
holes = []
order = []
cost = 0

def euclidean(p1, p2):
    res = math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    print("res1: ", res)
    res2 = np.linalg.norm(np.array(p1)-np.array(p2))
    print("res2: ", res2)

def readSolvedCluster(file):
    global numholes, holes
    with open(f'{file}', 'r') as reader:
        numholes = int(reader.readline())
        hole = reader.readline()
        while hole != '':
            coords = re.findall("\-?\d+\.\d+|\-?\d+", hole)
            holes.append((float(coords[0]), float(coords[1])))
            order.append(int(coords[2]))
            print(coords)
            hole = reader.readline()

def calculatePrice(holes, order):
    price = 0
    for i in range(numholes - 1):
        price = price + np.linalg.norm(np.array(holes[order[i]])-np.array(holes[order[i+1]]))
    return price

def processConnections():
    global cost
    connections = []
    directory = f'C:\\Users\\mn170387d\\Desktop\\clusters\\connections.txt'
    with open(directory,'r') as reader:
        for line in reader:
            coords = re.findall("\-?\d+\.\d+|\-?\d+", line) #x1 y1  (out curr) - x2 y2 (in next)
            outCurr = (float(coords[0]), float(coords[1]))
            inNext = (float(coords[2]), float(coords[3]))
            connections.append((outCurr,inNext))
    #lets remove the longest edge
    worstConn = 0
    worstDist = 0
    for i in range(len(connections)):
        dist = np.linalg.norm(np.array(connections[i][0])-np.array(connections[i][1]))
        cost = cost + dist
        if(dist>worstDist):
            worstDist = dist
            worstConn = i
    cost = cost - np.linalg.norm(np.array(connections[worstConn][0])-np.array(connections[worstConn][1]))
    del connections[worstConn]
    return connections


def main():
    global holes,order
    x = []
    y = []
    price = 0

    xfrom = 0
    xto = 300
    yfrom = -100
    yto = 0
    plt.figure(1, figsize=(16, 9), dpi=100)
    plt.style.use('seaborn-whitegrid')
    axes = plt.gca()
    axes.set_ylim(yfrom, yto)
    axes.set_xlim(xfrom, xto)

    directory = f'C:\\Users\\mn170387d\\Desktop\\clusters'
    for filename in os.listdir(directory):
        if 'solved' in filename:
            print("FAJL:", filename)
            x = []
            y = []
            holes = []
            order = []
            readSolvedCluster(os.path.join(directory, filename))
            price = price + calculatePrice(holes, order)
            for i in range(len(holes)):
                val = holes[order[i]]
                x.append(val[0])
                y.append(val[1])
                plt.plot(x, y)


    lista = processConnections()
    for i in lista:
        x = []
        y = []
        x.append(i[0][0])
        x.append(i[1][0])
        y.append(i[0][1])
        y.append(i[1][1])
        plt.plot(x,y)

    print("TOTAL COST: ", price+cost)
    plt.show()

    # for key, val in solved.items():
    #     print(key, ": ", val[0], " - ", val[1])
        # x.append(val[0])
        # y.append([val[1]])

    # price = calculatePrice(holes, order)
    # print("COST:",price)

if __name__ == '__main__':
    main()
