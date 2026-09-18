class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        days = []
        ans = []
        for x in reversed(temperatures):
            temp = 1
            while st:
                if x < st[-1]:
                    ans.append(temp)
                    st.append(x)
                    days.append(temp)
                    break
                else:
                    temp += days[-1]
                    st.pop()
                    days.pop()
            if not st: 
                ans.append(0)
                st.append(x)
                days.append(0)
        
        ans.reverse()
        return ans

                    
