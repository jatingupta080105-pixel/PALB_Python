from math import factorial

class Solution:
    def vowelCount(self, s):
        vowels = set("aeiou")
        freq = {}
        
        for ch in s:
            if ch in vowels:
                freq[ch] = freq.get(ch, 0) + 1
        
        if not freq:
            return 0
        
        ways = 1
        k = 0
        
        for v in freq:
            ways *= freq[v]
            k += 1
        
        return ways * factorial(k)