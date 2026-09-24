class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}" + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1: j+1+length])
            i = j + 1 + length
        return res
















    # def encode(self, strs: List[str]) -> str:
    #     encoded_string = ""
    #     for s in strs:
    #         encoded_string += str(len(s)) + "#" + s 
    #     return encoded_string

    # def decode(self, s: str) -> List[str]:
    #     strs = []
    #     i = 0
    #     while i < len(s):
    #         j = s.find("#", i)
    #         length=int(s[i:j])
    #         strs.append(s[j+1:j+1+length])
    #         i = j + 1 + length
    #     return strs
            

