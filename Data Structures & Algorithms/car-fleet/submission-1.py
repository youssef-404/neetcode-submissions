class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        speed_map = {}
        for i in range(len(speed)):
            speed_map[position[i]]=speed[i]

        position = sorted(position,reverse=True)

        for pos in position:
            last = -1
            if stack:
                last=(target-stack[-1])/speed_map[stack[-1]]
            current = (target-pos)/speed_map[pos]
            
            if current<= last:
                continue
            stack.append(pos)
        return len(stack)