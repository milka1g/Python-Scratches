import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

x = []
y = []
fix = []
num_clusters = 2


def main():
    global num_clusters
    xy = []
    with open(f'C:\\Users\\mn170387d\\Desktop\\clusters\\DBSCANcluster0.txt', 'r') as reader:
        line = reader.readline()
        print("Number of holes: ", line)
        line = reader.readline()
        while line != '':
            xy = line.split()
            fix.append([float(xy[0]), float(xy[1])])
            line = reader.readline()

    arr = np.array(fix)

    #####################KMEANS##################################

    clustered = False
    while not clustered:
        kmeans = KMeans(n_clusters=num_clusters,
                        n_init=20,
                        max_iter=600,
                        algorithm='full',
                        random_state=None)
        identified_clusters = kmeans.fit_predict(arr)

        print("The lowest SSE value:", kmeans.inertia_)

        #print("Cluster assignments:\n",identified_clusters)

        for i in range(len(identified_clusters)): #starting from 1 to make it from 0
            identified_clusters[i] = identified_clusters[i]-1

        dots_per_cluster = np.zeros(num_clusters)
        for i in range(len(identified_clusters)):
            dots_per_cluster[identified_clusters[i]] = dots_per_cluster[identified_clusters[i]] + 1

        new_num_clusters = num_clusters
        for i in range(len(dots_per_cluster)):
            if dots_per_cluster[i] > 16:
                new_num_clusters = new_num_clusters + 1
                break
        if new_num_clusters == num_clusters: #every cluster has <=15 dots
            clustered = True
        else:
            num_clusters = new_num_clusters

    sum = 0
    for i in range(len(dots_per_cluster)):
        sum = sum + dots_per_cluster[i]
    print("Final cluster numbers: ", dots_per_cluster, "\nsum: ", sum)

    #############################################################
    df = pd.DataFrame(arr, columns=['x', 'y'])
    df['clusters'] = identified_clusters
    plt.figure(1)
    plt.scatter(df['x'], df['y'], c=df['clusters'], cmap='rainbow')
    plt.show()



if __name__ == '__main__':
    main()

