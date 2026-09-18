class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        l_stack = []
        r_stack = []
        l_bound = []
        r_bound = []

        for x in heights: 
            temp = 0
            while len(l_stack) > 0:
                if l_stack[-1][0] < x:
                    l_stack.append((x,temp))
                    l_bound.append(temp)
                    break
                else:
                    temp += (l_stack[-1][1] +1)
                    l_stack.pop()
            if len(l_stack) == 0:
                l_stack.append((x,temp))
                l_bound.append(temp)

        for x in reversed(heights): 
            temp = 0
            while len(r_stack) > 0:
                if r_stack[-1][0] < x:
                    r_stack.append((x,temp))
                    r_bound.append(temp)
                    break
                else:
                    temp += (r_stack[-1][1] + 1)
                    r_stack.pop()
            if len(r_stack) == 0:
                r_stack.append((x,temp))
                r_bound.append(temp)


        r_bound.reverse()
        m = 0
        for i in range(len(heights)):
            m = max(m, heights[i]*(1+l_bound[i] + r_bound[i] ))
        return m
            
                    