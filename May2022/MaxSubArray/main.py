from common import *
n = 10  # number of testcases
roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
class Solution:
        def solutionGold(nums):
            dp = []
            dp.append(int(nums[0]))
            current_largest_sum = int(dp[0])
            for i in range(1, len(nums)):
                dp.append(max(int(dp[i - 1]) + int(nums[i]), int(nums[i])))
                if int(dp[i]) > current_largest_sum:
                    current_largest_sum = int(dp[i])
            return current_largest_sum
        def soluser(l):
            x = []
            k = -2
            return k;
for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/msa" + str(j+1) + ".txt") as f:
            content =f.readlines()
            l1=[x.strip() for x in content]
    except:
        print('Invalid testcase', testcaseNumber)
    obj = Solution()
    ans= obj.solutionGold(l1)
    userAns = obj.soluser(l1)
    check(ans,userAns,testcaseNumber)
count_cases()
