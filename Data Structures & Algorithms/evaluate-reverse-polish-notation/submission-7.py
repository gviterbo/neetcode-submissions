class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for x in tokens:
            if x == "+":
                a = int(s[-1])
                s.pop()
                b = int(s[-1])
                s.pop()
                s.append(b + a)
            elif x == "-":
                a = int(s[-1])
                s.pop()
                b = int(s[-1])
                s.pop()
                s.append(b - a)
            elif x == "*":
                a = int(s[-1])
                s.pop()
                b = int(s[-1])
                s.pop()
                s.append(b * a)
            elif x == "/":
                a = int(s[-1])
                s.pop()
                b = int(s[-1])
                s.pop()
                s.append(b /a)
            else:
                s.append(int(x))
        return int(s[0])

        