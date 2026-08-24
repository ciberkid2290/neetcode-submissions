class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            counts = {}

            for c in word:
                counts[c] = counts.get(c, 0) + 1

            key = tuple(sorted(counts.items()))
            
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        
        return list(groups.values())