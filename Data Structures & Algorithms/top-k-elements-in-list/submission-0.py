class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}

        for i in nums:
            counts[i] = counts.get(i,0) + 1
        
        res = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))

        fin = []
        for i,v in enumerate(res):
            if i<k:
                fin.append(v)
            else:
                break
    
        return fin