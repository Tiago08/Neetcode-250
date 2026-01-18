class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        start = strs[0]
        res = ""
        for s in range(len(start)):
            char = start[s]
            for w in strs[1:]:
                if s == len(w) or w[s] != char:
                    return res
            res += char




if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["a","a","a"]))