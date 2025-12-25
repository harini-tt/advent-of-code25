with open('input.in', 'r') as file:
    lines = file.readlines()
    grid = [list(lines[l].strip()) for l in range(len(lines))]
    m, n = len(grid), len(grid[0])
    print(grid)
    ans = 0
    for row_num in range(m):
        for col_num in range(n):
            if grid[row_num][col_num] == '@':
                tuples = (-1, 0, 1)
                count = 0
                for tx in tuples:
                    for ty in tuples:
                        if 0 <= row_num + tx < m and 0 <= col_num + ty < n:
                            if grid[row_num + tx][col_num + ty] == '@':
                                count += 1
                if count < 5:
                    ans += 1
    print(ans)
