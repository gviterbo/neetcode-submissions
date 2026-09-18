class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        order = []

        for i in range(len(position)):
            order.append((target-position[i], speed[i]))

        order.sort()
        
        t = []
        for a, b in order:
            t.append(a/b)
        
        stack = [t[0]]

        for x in t:
            if stack[-1] < x:
                stack.append(x)

        return len(stack)   