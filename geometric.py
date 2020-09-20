if __name__ == "__main__":
    import math
    def prob(n, p):
        '''
        - n: so lan thu
        - p: xac suat thanh cong cua 1 lan thu
        '''
        return p*pow(1-p, n - 1)
    
    def infoMeasure(n, p):

        return -math.log2(prob(n, p))

    def sumProb(N, p):
        '''
        - Bien luan sumProb -> 1 khi N->infinity
        - sumProb(100, 0.3) = 0.9999999999999992
        - sumProb(1000, 0.3) = 0.9999999999999996
        
        '''
        s = 0
        for x in range(1, N + 1):
            s += prob(x, p)    
        return s

    def approxEntropy(N, p):
        '''
        - approxEntropy(10, 0.5) = 1.98828125
        - approxEntropy(100, 0.5) = 1.9999999999999998
        => N->inf => approxEntropy(N, p) -> 2
        '''
        s = 0
        for x in range(1, N + 1):
            s += infoMeasure(x, p)*prob(x, p)
        return s
    print(approxEntropy(100, 0.5))