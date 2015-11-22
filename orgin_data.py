import pylab as pl


def main():
    origin = open('origin10.txt', 'r')

    lines = origin.readlines()

    normal_x = []
    normal_y = []
    attack_x = []
    attack_y = []

    for l in lines:
        l = l.split(',')
        if l[-1] == 'normal.\n':
            normal_x.append(float(l[32]))
            normal_y.append(float(l[35]))
        else:
            attack_x.append(float(l[32]))
            attack_y.append(float(l[35]))

    pl.plot(normal_x, normal_y, 'ro')
    pl.plot(attack_x, attack_y, 'go')

    pl.show()

if __name__ == '__main__':
    main()