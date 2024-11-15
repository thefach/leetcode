class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for _ in range(0, len(nums)):
            if  nums[k] == val:
                nums.remove(nums[k])
            else:
                k+=1


        



        