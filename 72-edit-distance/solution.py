class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #so at each word, you are allowed to do one thing
        #replace word1's last char with word2's
        #delete word1's curr char
        #insert char1
        m, n = len(word1), len(word2)
        #should be m + 1 rows and n + 1 columns

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        #dp[i][j] will be the cost of getting word1[0:i] to word2[0:j]

        #cases
        #1: word1[:i] -> 0
        #delete i chars

        for i in range(m + 1):
            dp[i][0] = i
        
        #2: "" -> word2[j:]
        #add j chars
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                
                else:
                    delete = dp[i-1][j]
                    #if you delete char from word1, its just one less

                    insert = dp[i][j-1]
                    replace = dp[i-1][j-1]

                    dp[i][j] = 1 + min(delete, insert, replace)

        return dp[m][n]


#idea for this is because there are multiple diverging paths and going back: use dp
#dp will store the minimum cost to convert word1[:i] to word2[:j]
#so dp[i][j] = the minimum cost to convert the first i chars of word1 to the first j chars of word2

#and then after that, need to set baselines
#word[:i] -> "" (deleting i)
#"" -> word[:j] (inserting j)

#this fills in the top and the left

#once that, can iterate throught i, j pairs
#does this in row major order 

#and then first check if found it already (if last chars match)
#if word1[i-1] == word2[j-1] then set dp[i][j] to dp[i-1][j-1]

#if thats not true
#go through options of delete, insert, and replace
#each one costs 1 so add 1 to the min cost of each of the three
#delete takes one away from word1
#so dp[i-1][j]
#insert takes one away from word2
#so dp[i][j-1]
#replace from both so dp[i-1][j-1]

#then do dp[i][j] = 1+ min (replace, delete, insert) 

#and lastly return [m][n] as the answer of min cost

#Time: O(m * n) where m and n are lengths of each word
#Space: O(m * n)
