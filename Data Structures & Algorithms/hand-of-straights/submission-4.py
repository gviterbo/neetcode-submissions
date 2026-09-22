class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        
        hist = [0]*(max(hand)+1)
        for x in hand:
            hist[x] += 1
        op = [0]*len(hist)
        s = 0

        for i in range(len(hist)):
            
            hist[i] = hist[i] + s
            s += op[i]
    
            if hist[i] > 0:
                temp = hist[i]
                s -= hist[i]
                hist[i] = 0
                if i + groupSize-1 >= len(hist):
                    return False
                op[i+groupSize-1] = temp
                if groupSize-1 == 0:
                    s += temp
        for x in hist:
            if x != 0:
                return False
        
        return True


            