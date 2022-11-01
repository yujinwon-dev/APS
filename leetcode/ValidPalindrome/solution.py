class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted = []
        # 알파벳, 숫자만 converted에 push
        for char in s:
            if char.isalpha():
                converted.append(char.lower())
            elif char.isdecimal():
                converted.append(char)
        length = len(converted)
        # 팰린드롬 확인
        for i in range(length // 2):
            if converted[i] != converted[length - 1 - i]:
                return False
        return True
