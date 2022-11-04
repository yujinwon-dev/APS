# 아래와 같이 풀 경우 n_idx 가 0보다 크면서 현재 위치부터 needle 을 비교할 경우 새롭게 조건을 통과할 때를 캐치하지 못함
# ex) haystack = "mississippi" 이고 needle = "issip" 일 때,
#     h_idx=1일 때부터 "issi" 만큼 만족하지만 h_idx=4일 때 n_idx 가 0이어야 정답이 됨
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_length = len(needle)
        h_length = len(haystack)
        n_idx = 0
        if needle not in haystack:
            return -1
        for h_idx in range(h_length):
            if n_idx == n_length:
                return h_idx - n_length
            if haystack[h_idx] == needle[n_idx]:
                n_idx += 1
            else:
                n_idx = 0
        if n_idx == n_length:
            return h_length - n_length


s = Solution()
print(s.strStr("mississippi", "issip"))
