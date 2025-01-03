class Solution:
    def reverseBits(self, n: int) -> int:
        b=bin(n)
        b=b[2::]
        b=str(b)
        b=b[::-1]
        while(1):
            if len(b)<32:
                b+='0'
            else:
                break
        return int(b,2)
