#--*--coding=utf-8--*--

def squared_distance(k,q):
    return sum([(k_i-q_i)**2 for k_i,q_i in zip(k,q)])

def mean(t):
    return float(sum(t))/len(t)

def vector_mean(vectors):
    return [mean(


class KMeans(object):
    def __init__(self,k):
        self.k = k
        self.means = None

    def classify(self,input):
        return min(range(self.k),
               key=lambda i: squared_distance(input, self.means[i]))

    def train(self,inputs)
