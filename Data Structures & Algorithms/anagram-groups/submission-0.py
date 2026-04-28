class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}

        for st in strs:
            curr = "".join(sorted(st))
            if curr not in data:
                data[curr] = []
            data[curr].append(st)
        
        return [x for x in data.values()]
            
