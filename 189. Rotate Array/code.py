class Solution:
    def rotate(self, nums , k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums=nums[k+1:]+nums[:k+1]
        print(nums)
        
temp=Solution()
temp.rotate([1,2,3,4,5,6,7], 3)