class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        if n == 0:
            return 0

        groups = []
        i = 0

        while i < n:
            count = 1
            while i + 1 < n and word[i] == word[i + 1]:
                count += 1
                i += 1
            groups.append(count)
            i += 1

        total = 1 
        for count in groups:
            if count > 1:
                total += count - 1  

        return total

