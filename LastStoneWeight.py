import heapq

class Solution:
    def lastStoneWeight(self, stones): 

        #create a max heap by negating the stone weights bc heapq is a min heap by default
        max_heap = [-s for s in stones] #negate the stone weights
        heapq.heapify(max_heap) #transform list into a heap in O(n) time

        #we'll smash the stones
        while len(max_heap) > 1: #while there are at least two stones to smash
            first = -heapq.heappop(max_heap)  #heaviest stone
            second = -heapq.heappop(max_heap) #second heaviest stone

            #if they aren't equal, push the difference(leftover stone) back into the heap
            if first != second:
                heapq.heappush(max_heap, -(first - second))

        #return the weight of the last stone or 0 if none left
        return -max_heap[0] if max_heap else 0

#Test Example 1; Output = 1
stones = [2,7,4,1,8,1]
print(Solution().lastStoneWeight(stones))

#Test Example 2; Output = 1
stones = [1]
print(Solution().lastStoneWeight(stones))  
