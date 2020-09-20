if __name__ == "__main__":
    import math
    import numpy

    def nCk(N, k) : 
        return numpy.prod([(N-k+i)/i for i in range(1, k+1)])
    
    def prob(n, p, k):
        '''
        - n: so lan thu
        - p: xac suat thanh cong cua 1 lan thu
        '''
        return nCk(n, k)*(p**k)*((1-p)**(n-k))
    
    def infoMeasure(n, p, k):
        return -math.log2(prob(n, p, k))

    def sumProb(N, p):
        
        s = 0
        for k in range(1, N + 1):
            s += prob(N, p, k)    
        return s

    def approxEntropy(N, p):
        s = 0
        for k in range(1, N + 1):
            s += infoMeasure(N, p, k)*prob(N, p, k)
        return s
    print(approxEntropy(100, 0.5))
    