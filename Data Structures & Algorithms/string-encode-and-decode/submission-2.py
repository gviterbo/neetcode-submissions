class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "v"
        ans = []
        for x in strs:
            temp = []
            for c in x: 
                temp.append(str(ord(c)))
            if temp == []:
                temp = ['n']
            s = "#".join(temp)
            ans.append(s)
        return ",".join(ans)

    def decode(self, s: str) -> List[str]:
        if s == "v":
            return []
        ans = []
        string = s.split(",")
        for x in string:
            temp = []
            l = x.split("#")
            for y in l:
                if y == 'n':
                    temp.append("")
                    break
                else:
                    temp.append(chr(int(y)))
            ans.append("".join(temp))
        return ans