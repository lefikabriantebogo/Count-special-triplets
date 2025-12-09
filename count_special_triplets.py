class Solution(object):
    def specialTriplets(self, nums):
        MOD = 10 ** 9 + 7

        from collections import Counter

        right = Counter(nums)
        left = Counter()

        ans = 0

        for j in range(len(nums)):
            val = nums[j]
            right[val] -= 1  # remove j from future candidates

            target = val * 2

            # count valid i and k
            count_left = left[target]
            count_right = right[target]

            ans = (ans + count_left * count_right) % MOD

            left[val] += 1  # add j to left for future

        return ans % MOD
