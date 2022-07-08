from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,S,x):
            m=len(S)
            table = [0 for k in range(x+1)]
            table[0] = 1
            for i in range(0,m):
                for j in range(int(S[i]),x+1):
                    table[j] += table[j-int(S[i])]
            return table[x]

        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/cc" + str(j+1) + ".txt") as f:
            #num=int(f.read())
            content =f.readlines()
            num=[x.strip() for x in content]
            #if num.length()<3 or num.length()>1000:
                #print("Please enter an array of size in range of [3,1000]; testcase-",testcaseNumber)
        with open("testcases/cc1" + str(j+1) + ".txt") as f:
            sum=int(f.read())
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(num,sum)
    userAns = obj.soluser(num)
    check(ans, userAns, testcaseNumber)

count_cases()