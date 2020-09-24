from bitstring import BitStream, BitArray

class PrefixCodeTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert (self, codebook, symbol):
        for i in codebook:
            if (i == 0):
                if (self.left == None):
                    self.left = PrefixCodeTree(-1)
                self = self.left
            elif (i == 1):
                if (self.right == None):
                    self.right = PrefixCodeTree(-1)
                self = self.right
        self.data = symbol
        
    def decode(self, encodedData, datalen):
        byte = BitArray(bytes=encodedData, length=datalen)
        s = byte.bin
        res = ''
        curr = self
        for i in s:
            if (i == '0'):
                curr = curr.left
            elif (i == '1'):
                curr = curr.right
            if (curr.data != -1):
                res += curr.data
                curr = self
        return res            
            
codebook = {
'x1': [0],
'x2': [1,0,0],
'x3': [1,0,1],
'x4': [1,1]
}

codeTree = PrefixCodeTree(10)
for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)
message = codeTree.decode(b'\xd2\x9f\x20', 21)
print(message)

