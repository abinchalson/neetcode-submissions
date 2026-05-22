from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for s in strs:
            signature = ''.join(sorted(s))
            grouped[signature].append(s)
        return list(grouped.values())    



        