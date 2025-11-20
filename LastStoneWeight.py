import heapq

class Solution:
    def lastStoneWeight(self, stones): #lastStoneWeight takes in the list of stone weights

        #since heapq is a min heap by default, we create a new max heap, storing all the numbers as negatives
        max_heap = [-s for s in stones] #negate the stone weights
        heapq.heapify(max_heap) #transform list into a heap structure, removing the heaviest stone 

        #where we smash at least two stones, stopping when there's less than 1
        while len(max_heap) > 1: #while there are at least two stones to smash
            first = -heapq.heappop(max_heap)  #heaviest stone
            second = -heapq.heappop(max_heap) #second heaviest stone

            #if they aren't equal, push the difference(leftover stone) back into the heap
            if first != second:
                heapq.heappush(max_heap, -(first - second))

        #return the weight of the last stone if theres any left or 0 if none are left
        return -max_heap[0] if max_heap else 0

#Test Example 1; Output = 1
stones = [2,7,4,1,8,1]
print(Solution().lastStoneWeight(stones))

#Test Example 2; Output = 1
stones = [1]
print(Solution().lastStoneWeight(stones))  
