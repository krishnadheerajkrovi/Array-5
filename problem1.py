'''
1. This involved the concept of Limit Cycle Trajectory. At max 4 cycles later if it doesnt reach the starting point, we can say it is diverging
2. To further prevent us from running 4 cycles, we can check if it points to north (which it did initially)

TC: O(n)
SC: O(1)
'''

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # north = 0, east = 1, south = 2, west = 3
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        cur_dir = 0
        cur_x = 0
        cur_y = 0
        for i in instructions:
            if i == 'G':
                cur_x +=  dirs[cur_dir][0]
                cur_y +=  dirs[cur_dir][1]

            elif i == 'L':
                cur_dir = (cur_dir + 1) % 4
            else:
                cur_dir = (cur_dir + 3) % 4
        
        return (cur_x == 0 and cur_y ==  0) or cur_dir != 0
            



        