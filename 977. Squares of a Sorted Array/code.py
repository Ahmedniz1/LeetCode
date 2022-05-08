class Solution:
    def sortedSquares(self, nums):
        left,right=0,len(nums)-1
        output=[]
        for i in range(len(nums)):
            l,r=abs(nums[left]),abs(nums[right])
            print(l,r)
            if l>r:
                output.append(l*l)
                left+=1
            else:
                output.append(r*r)
                right-=1
        return output[::-1]
            
temp=Solution()
print(temp.sortedSquares([-4,-1,0,3,10]))