import numpy as np
with open('input.in', 'r') as file:
    lines = file.readlines()
    grid = [lines[l].strip().split() for l in range(len(lines))]
    ops = grid.pop()
    transposed_grid = np.array(grid, dtype='int').T
    print(transposed_grid)
    m = len(transposed_grid[0])
    ans = 0
    for op in range(len(ops)):
        mid_ans = transposed_grid[op][0]
        for i in range(1, m):
            if ops[op] == '*':
                mid_ans *= transposed_grid[op][i]
            else:
                mid_ans += transposed_grid[op][i]
        
        ans += mid_ans
    print(ans)
