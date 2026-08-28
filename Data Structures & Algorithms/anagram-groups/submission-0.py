class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        index = {}

        for i,s in enumerate(strs):
            sortedS =''.join(sorted(s))
            value = index.get(sortedS,[])
            value.append(strs[i])
            index[sortedS] = value
    

        results = []
        for s in index:
            results.append(index[s])
        return results