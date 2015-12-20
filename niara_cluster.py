import numpy as np
from sklearn.cluster.bicluster import SpectralCoclustering
from datetime import datetime


def main():
    origin = open('10k.txt', 'r')

    lines = origin.readlines()

    x = []
    label = []

    for l in lines:
        l = l.split(',')
        ip1 = l[2].split('.')
        ip2 = l[3].split('.')
        d = [datetime.fromtimestamp(int(l[1][0:11])).hour, int("%02x%02x%02x%02x"%(int(ip1[0]),int(ip1[1]),int(ip1[2]),int(ip1[3])),16), int("%02x%02x%02x%02x" % (int(ip2[0]),int(ip2[1]),int(ip2[2]),int(ip2[3])),16)] + l[4:6] + l[7:10]
        x.append(d)

    data = np.array(x, dtype='float32')

    model = SpectralCoclustering(n_clusters=5)
    model.fit(data)

    print model.rows_

    for i in range(5):
        print "Cluster" + str(i) + ':'
        for j in range(10000):
            if model.rows_[i][j]:
                print j,
        print ' '


if __name__ == '__main__':
    main()
