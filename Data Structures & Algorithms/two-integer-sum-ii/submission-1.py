class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        counter = {}

        for index,value in enumerate(numbers):
            if target - value in counter:
                return [counter[target - value]+1,index+1]
            counter[value]=index

