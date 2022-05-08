import collections
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        while True:
            if nums[i:]==[0]*len(nums[i:]):
                break

            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
                i-=1
            i+=1
                



        print(nums)
temp=Solution()
temp.moveZeroes([0,4,0,1,0,3,12])
temp.moveZeroes([0,1,0,3,12])
temp.moveZeroes([0,0,1])
