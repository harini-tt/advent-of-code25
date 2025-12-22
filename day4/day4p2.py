with open('input.in', 'r') as file:
    def del_all(m, n):
        ans = []
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
                        ans.append((row_num, col_num))
        for tup in ans:
            grid[tup[0]][tup[1]] = '.'
        return len(ans)
    
    lines = file.readlines()
    grid = [list(lines[l].strip()) for l in range(len(lines))]
    m, n = len(grid), len(grid[0])
    final_ans = 0
    prev = 1
    final_ans = del_all(m, n)
    prev_round = final_ans
    while prev_round != 0:
        prev_round = del_all(m, n)
        final_ans += prev_round
    print(final_ans)
