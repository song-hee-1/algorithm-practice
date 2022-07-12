# leetcode : 937 Reorder Log Files
from typing import List


# 람다와 + 연산자를 이용한 풀이
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # 두 개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits