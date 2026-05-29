class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n=len(nums)
        s=0
        k=0
        final=[]
        for i in range(len(nums)-2):
            a=nums[i]
            right=n-1
            pointer=i+1
            #check duplicate
            if i>0 and nums[i]==nums[i-1]:
                continue  
            while pointer<right:
                s=nums[i]+nums[right]+nums[pointer]
                if s==0:
                    k+=1