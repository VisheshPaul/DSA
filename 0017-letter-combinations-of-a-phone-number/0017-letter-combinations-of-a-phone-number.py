class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        h = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        l = []
        for i in digits:
            l.append(h[int(i)])
        print(l)
        ans = []
        def func(x,index):
            if index == len(digits):
                ans.append("".join(x))
                return 
            for i in l[index]:
                x.append(i)
                func(x,index+1)
                x.pop()
        func([],0)
        return ans
                