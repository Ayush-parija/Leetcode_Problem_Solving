MOD = 10**9 + 7

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        from itertools import groupby
        

        run_lengths = [len(list(group)) for _, group in groupby(word)]
        
       
        total = 1
        for p in run_lengths:
            total = (total * p) % MOD
        
        
        if sum(run_lengths) < k:
            return 0
        if len(run_lengths) >= k:
            return total
        
       
        n = len(run_lengths)
        max_len = k - 1
        prev = [0] * (max_len + 1)
        prev[0] = 1  

        for i in range(n):
            curr = [0] * (max_len + 1)
            prefix = [0] * (max_len + 2) 
            for j in range(max_len + 1):
                prefix[j + 1] = (prefix[j] + prev[j]) % MOD

            for j in range(1, max_len + 1):
                left = max(0, j - run_lengths[i])
                right = j
                curr[j] = (prefix[right] - prefix[left]) % MOD

            prev = curr

        
        short_results = sum(prev) % MOD

       
        return (total - short_results + MOD) % MOD
