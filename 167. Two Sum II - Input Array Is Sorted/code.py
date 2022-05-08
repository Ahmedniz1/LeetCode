class Solution:
    def twoSum(self, numbers , target):
        start,end=0,len(numbers)-1
        while True:
            sum=numbers[start]+numbers[end]
            print(sum,start,end)
            if sum==target:                
                return start+1,end+1
            elif sum>target:
                end=end//2
            elif sum<target:
                start=end//2
            if start>end:
                break
temp=Solution()
print(temp.twoSum([2,7,11,15], 22))