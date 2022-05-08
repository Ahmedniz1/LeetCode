class Solution:
    def maxOperations(self, nums, k) -> int:
        dic={}
        for n in nums:
            flag=False
            if len(dic)==0:
                dic[n]=[n,1]
            else:
                keys=dic.keys()
                temp_key=float("-inf")
                for key in keys:
                    if key+n==k:
                        dic[key]=[k,2]
                        flag=True
                        break
            if not flag:
                dic[n]=[n,1]
            flag=False
        vals=dic.values()
        count=0
        for val in vals:
            if val[0]==k and val[1]==2:
                count+=1
        return count
temp=Solution()
temp.maxOperations([3,1,5,1,1,1,1,1,2,2,3,2,2], 1)