class Solution:
    def groupAnagrams(self, strs):
        a=defaultdict(list)
        for i in strs:
            temp=list(i)
            temp.sort()
            word=''.join(temp)
            a[word].append(i)
        b=[]
        for i in a.values():
            b.append(i)
        return b
