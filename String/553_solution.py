class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums)==1:
            return str(nums[0])
        elif len(nums)==2:
            return str(nums[0])+'/'+str(nums[1])
        else:
            out=str(nums[0])+"/("+'/'.join(map(str,nums[1:]))+")"
            return  out
