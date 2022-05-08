class Solution:
    def find132pattern(self, nums) -> bool:
        my_stack=[]
        s3=float('-inf')
        for n in nums[::-1]:
            if n<s3: return True
            while my_stack and my_stack[-1]<n: s3=my_stack.pop()
            my_stack.append(n)
        return False
temp=Solution()
print(temp.find132pattern([1,0,1,-4,-3]))