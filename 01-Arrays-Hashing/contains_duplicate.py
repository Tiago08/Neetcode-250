class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        check = []
        for n in nums:
            if n in check:
                return True
            check.append(n)
        return False



if __name__ == "__main__":
    sol = Solution()
    print(sol.hasDuplicate([1, 2, 3, 3]))