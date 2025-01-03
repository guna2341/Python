class Solution:
    def trailingZeroes(self, n: int) -> int:
        a=0
        while n>0:
            n=n//5
            a=a+n
        return a
