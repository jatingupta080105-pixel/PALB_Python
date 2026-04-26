from collections import defaultdict

class Solution:
    def winner(self, arr):
        freq = defaultdict(int)
        
        # count votes
        for name in arr:
            freq[name] += 1
        
        max_votes = 0
        winner_name = ""
        
        for name in freq:
            if freq[name] > max_votes:
                max_votes = freq[name]
                winner_name = name
            elif freq[name] == max_votes:
                if name < winner_name:
                    winner_name = name
        
        return [winner_name, str(max_votes)]