class Solution:
    def checkValidString(self, s: str) -> bool:
        st = []
        ast = []
        for i in range(len(s)):
            x = s[i]
            if x == '*':
                ast.append([i, '*'])
                continue
            if not st:
                st.append([i, x])
            elif x == ')' and st[-1][1] == '(':
                st.pop()
            else:
                st.append([i, x])
        
        for x in st:
            ast.append(x)
        ast.sort()
        print(ast)
        st = []

        for t in ast:
            x = t[1]
            if not st:
                st.append(x)
            elif x == ')' and st[-1] != x:
                st.pop()
            elif x == '*' and st[-1] == '(':
                st.pop()
            else:
                st.append(x)
        print(st)
        for x in st:
            if x != '*':
                return False
        return True



        