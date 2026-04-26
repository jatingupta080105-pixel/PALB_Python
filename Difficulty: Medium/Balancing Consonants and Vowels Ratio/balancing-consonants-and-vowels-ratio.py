class Solution:
    def countBalanced(self, arr):
        def is_vowel(ch):
            return ch in "aeiou"
        
        prefix = 0
        freq = {0: 1}
        ans = 0
        
        for s in arr:
            bal = 0
            
            for ch in s:
                if is_vowel(ch):
                    bal += 1
                else:
                    bal -= 1
            
            prefix += bal
            
            ans += freq.get(prefix, 0)
            freq[prefix] = freq.get(prefix, 0) + 1
        
        return ans