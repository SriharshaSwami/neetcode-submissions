class Solution:
    lengths=[]
    def encode(self, strs: List[str]) -> str:
        for string in strs:
            self.lengths.append(len(string))
        print(''.join(strs),self.lengths)
        return ''.join(strs)
    def decode(self, s: str) -> List[str]:
        start,end=0,0
        result=[]
        for i in self.lengths:
            end+=i
            result.append(s[start:end])
            start=end
        return result

