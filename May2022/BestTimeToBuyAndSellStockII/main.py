from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self, prices: List[int]) -> int:
            res = 0
            for i in range(len(prices)-1):
                if -abs(int(prices[i])) + int(prices[i+1]) > 0:
                    res += -abs(int(prices[i])) + int(prices[i+1])
            return res
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/bt2" + str(j+1) + ".txt") as f:
            #num=int(f.read())
            content =f.readlines()
            num=[x.strip() for x in content]
        #if num.length()<3 or num.length()>1000:
            #print("Please enter an array of size in range of [3,1000]; testcase-",testcaseNumber)
        
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(num)
    userAns = obj.soluser(num)
    check(ans, userAns, testcaseNumber)

count_cases()