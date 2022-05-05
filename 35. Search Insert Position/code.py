class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            middle=left+(right-left)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]>target:
                if 0==middle and nums[middle]>target:
                    return 0
                if nums[middle-1]<target:
                    return middle
                right=middle-1
            elif nums[middle]<target:
                if len(nums)==middle+1 and nums[middle]<target:
                    return middle+1
                if nums[middle+1]>target:
                    return middle+1
                left=middle+1
        return -1