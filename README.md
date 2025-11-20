# leetcode_LastStoneWeight

**PROBLEM:** You are given an array of integers stones where stones[i] is the weight of the ith stone. We play a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x ≤y. The result of this smash is:
• If x == y, both stones are destroyed.
• If x ̸= y, the stone of weight x is destroyed, and the stone of weight y has new weight y−x.

At the end of the game, there is at most one stone left. Return the weight of the last remaining
stone. If there are no stones left, return 0.

**WHY IT WORKS:**
This works as it's always picking between the two largest stones, which satisfies the greedy choice concept, and smashing them depending on whether they're equal or different, repeating until there's at least 1 stone left. If they're equal, both stones are smashed, but if they're different, we put back the difference. It's optimal we pick the heaviest stone, so we can remove as much weight as possible each time.

**GREEDY CHOICE:**


**COMPLEXITY:**

