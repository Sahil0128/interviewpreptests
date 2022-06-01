from common import *
n = 10  # number of testcases
countPassed=0
countFailed=0 
for j in range(n):
    testcaseNumber=j+1
    try:
        with open("testcases/vp" + str(j+1) + ".txt") as f:
        s1=f.read()
    except:
        print('Invalid testcase')
    def solutionGold(s):
        pair = dict(('()', '[]', '{}'))
        st = []
        for x in s:
            if x in '([{':
                st.append(x)
            elif len(st) == 0 or x != pair[st.pop()]:
                return False
        return len(st) == 0
    ans=solutionGold(s1)
    def soluser(s):
        #wrong solution
        x=[]
        k=2
        return False;
    userAns=soluser(s1)
    check(ans,userAns,testcaseNumber)
count_cases()
