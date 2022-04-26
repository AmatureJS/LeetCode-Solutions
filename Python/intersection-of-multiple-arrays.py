# Time:  O(n * l + r), n = len(nums), l = len(nums[0]), r = max(nums)-min(nums)
# Space: O(l)

# set, counting sort
class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        result = set(nums[0])
        for i in xrange(1, len(nums)):
            result = set(x for x in nums[i] if x in result)
        return [i for i in xrange(min(result), max(result)+1) if i in result] if result else []


# Time:  O(n * l + llogl), n = len(nums), l = len(nums[0])
# Space: O(l)
# set, sort
class Solution2(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        result = set(nums[0])
        for i in xrange(1, len(nums)):
            result = set(x for x in nums[i] if x in result)
        return sorted(result)
