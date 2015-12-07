import numpy as np
from sklearn.cluster.bicluster import SpectralCoclustering
import pylab as pl


def main():
    origin = open('kddcup.txt', 'r')

    lines = origin.readlines()

    x = []
    label = []

    for l in lines:
        l = l.split(',')
        d = l[0:1] + l[4:19] + l[21:-1]
        label.append(l[-1])
        x.append(d)

    data = np.array(x, dtype='float32')

    model = SpectralCoclustering(n_clusters=5)
    model.fit(data)

    evaluation = []

    draw_n_x = []
    draw_n_y = []
    draw_a_x = []
    draw_a_y = []

    for cluster in model.rows_:
        normal = 0.0
        attack = 0.0
        graph_x = []
        graph_y = []
        for idx in range(len(cluster)):
            if cluster[idx]:
                if label[idx] == 'normal.\n':
                    normal += 1
                else:
                    attack += 1
                graph_x.append(data[27])
                graph_y.append(data[30])
        evaluation.append(normal / (normal + attack))

        if normal > attack:
            draw_n_x += graph_x
            draw_n_y += graph_y
        else:
            draw_a_x += graph_x
            draw_a_y += graph_y

    pl.plot(draw_n_x, draw_n_y, 'ro')
    pl.plot(draw_a_x, draw_a_y, 'go')

    print evaluation
    pl.show()

if __name__ == '__main__':
    main()
