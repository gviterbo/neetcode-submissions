class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for i in range(len(s)):
            x = s[i]
            if len(st) == 0:
                st.append(x)
            elif x == ')' and st[-1] == '(':
                st.pop()
            elif (x == '}' and st[-1] == '{'):
                st.pop()
            elif (x == ']' and st[-1] == '['):
                st.pop()
            else:
                st.append(x)

        if len(st) == 0:
            return True
        else:
            return False

        