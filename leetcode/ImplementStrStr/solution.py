class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        return haystack.index(needle)


s = Solution()
print(s.strStr("mississippi", "issip"))
