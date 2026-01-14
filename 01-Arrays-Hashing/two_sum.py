class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        new_dict = {}
        for i,n in enumerate(nums):
            diff = target - n

            if diff in new_dict:
                return [new_dict[diff], i]
            new_dict[n] = i


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum(nums = [5,5], target = 10))