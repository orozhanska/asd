# adjacency matrix
# solution is not the best at all by the complexity, but I do not touch what works
# time complexity is O(n^2) as we first check the values on horizontal, then on wertical axis
# Space complexity is O(n^2) as we store the matrix with n^2 values
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # adj matrix
        if n == 1:
            return 1
            
        matrix = [[0] * n for _ in range (n)]
        
        for t in trust:
            ox, oy = t[0], t[1]
            matrix[ox-1][oy-1] = 1


        for ox in range(n):
            is_judge = False
            if matrix[ox] == [0] * n:
                is_judge = True
                for oy in range(n):
                    if (matrix[oy][ox] != 1) and (ox != oy):
                        is_judge = False
            if is_judge:
                return ox+1
        
        return -1

# hashmap
# Time O(n+k) where k is the length of trust
# Space O(n) as we store the results in a list

class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # hashtable
        if n == 1:
            return 1
        # we take the № of person as an index in hashmap
        hashmap = [[0, 0] for _ in range(n+1)]

        for a, b in trust:
            hashmap[a][0] +=1
            hashmap[b][1] +=1
        
        for i in range(1, n+1):
            trust_item = hashmap[i]
            if trust_item[0] == 0 and trust_item[1] == n - 1:
                return i
            
        return -1

# In my implementation hashmap is better



