class Solution:
    def myAtoi(self, s: str) -> int:
        # 문자열 앞의 연속된 공백만 제거하기 위해 strip 사용 (replace(" ", "") => x)
        s = s.strip()
        if not s:
            return 0
        sign = 1
        idx = 0
        start = 0
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                sign = -1
            idx += 1
            start += 1
        length = len(s)
        while idx < length and s[idx].isdigit():
            idx += 1
        result_str = s[start:idx]
        result = int(result_str) * sign if result_str else 0
        if result < -2 ** 31:
            return -2 ** 31
        elif 2 ** 31 <= result:
            return 2 ** 31 - 1
        return result
        