from collections import defaultdict

with open("input.in") as f:
    grid = [list(line.rstrip("\n")) for line in f if line.rstrip("\n") != ""]
m, n = len(grid), len(grid[0])

sr = sc = None
for r in range(m):
    for c in range(n):
        if grid[r][c] == "S":
            sr, sc = r, c
            break
    if sr is not None:
        break

active = {sc: 1}
for r in range(sr, m - 1):
    next_active = defaultdict(int)
    for c, ways in active.items():
        if grid[r + 1][c] == "^":
            if c - 1 >= 0:
                next_active[c - 1] += ways
            if c + 1 < n:
                next_active[c + 1] += ways
        else:
            next_active[c] += ways
    active = next_active

print(sum(active.values()))
