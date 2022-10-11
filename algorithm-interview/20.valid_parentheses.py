# leetcode : 20 Valid Parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        S = []

        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for symbol in s:
            if symbol not in table:
                S.append(symbol)
            elif not S or table[symbol] != S.pop():
                return False

        return len(S) == 0
