class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = nums * 2
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.getConcatenation([1,4,1,2]))