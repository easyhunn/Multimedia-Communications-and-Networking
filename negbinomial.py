if __name__ == "__main__":
    import math
    import numpy

    def nCk(N, k) : 
        return numpy.prod([(N-k+i)/i for i in range(1, k+1)])
    
    def prob(k, p, r):
        '''
        - n: so lan thu
        - p: xac suat thanh cong cua 1 lan thu
        '''
        return nCk(k, k-r+1) * (p**r) * ((1-p)**(k-r))  
    
    def infoMeasure(k, p, r):
        return -math.log2(prob(k, p, r))

    def sumProb(N, p, r):
        
        s = 0
        for k in range(1, N  + 1):
            s += prob(k, p, r)    
        return s

    def approxEntropy(N, p, r):
        s = 0
        for k in range(1, N + 1):
            s += infoMeasure(k, p, r)*prob(k, p, r)
        return s
    print(approxEntropy(100, 0.5, 5))
    