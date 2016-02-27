class Solution(object):
    #1 [0,0]   0
    #2 [3,2,4] 6
    # 方法: 边记录信息,边处理
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, n in enumerate(nums): 
            if target-n in dic:
                return [dic[target-n], i]
            dic[n] = i
