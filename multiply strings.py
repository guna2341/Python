class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a=num1[0::]
        b=num2[0::]
        c=0
        d=0
        for i in a:
            c=c*10+int(i)
        for i in b:
            d=d*10+int(i)
        e=c*d
        return str(e)
