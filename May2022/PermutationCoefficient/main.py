from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self, nums: List[int]) -> int:
            f=1
            for i in range(int(nums[1])):
                f*=(int(nums[0])-i)
            #print(f)
            return f
        def soluser(self, num):
            x = []
            k = -2
            return x

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/pc" + str(j+1) + ".txt") as f:
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