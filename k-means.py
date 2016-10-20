#--*--coding=utf-8--*--
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random


def squared_distance(v,w):
    return sumofsquares(vector_subs(v,w))

def mean(t):
    return float(sum(t))/len(t)

def dot(v,w):
    return sum(vi*wi for vi,wi in zip(v,w))

def sumofsquares(v):
    return dot(v,v)

def vector_subs(v,w):
    return [vi-wi for vi,wi in zip(v,w)]

def vector_add(v,w):
    return [vi-wi for vi,wi in zip(v,w)]

def vector_mean(vectors):
    sumv = []
    for vector in vectors:
        sumv = vector_add(sumv,vector)
    l=len(vectors)
    return [float(v)/l for v in sumv]

class KMeans(object):
    def __init__(self,k):
        self.k = k
        self.means = None

    def classify(self,input):
        return min(range(self.k),
               key=lambda i: squared_distance(input, self.means[i]))

    def train(self,inputs):
        assignments = None
        self.means = random.sample(inputs,self.k)
        while True:
            new_assignments = map(self.classify,inputs)

            if new_assignments == assignments:
                return
            assignments = new_assignments

            for i in range(self.k):
                i_points = [p for p, a in zip(inputs,assignments) if a == i]
                if i_points:
                    self.means[i] = vector_mean(i_points)

if __name__ == '__main__':
    path = '/home/boxiao/1.jpg'
    img = mpimg.imread(path)
    pixs = [pix for row in img for pix in row]

    cluster = KMeans(5)
    cluster.train(pixs)
    print cluster.means

    def recolor(pixel):
        cluster1 = cluster.classify(pixel)
        return cluster.means[cluster1]

#    new_img = [[recolor(pix) for pix in row] for row in img]
    print 'start to show pic'

#    with open('t.txt','w') as f:
 #       for i in new_img:
  #          f.write(str(i)+'\n')

    plt.imshow(img)
    plt.axis('off')
    plt.show()
