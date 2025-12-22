with open("input.in") as f:
    grid = [list(line.rstrip("\n")) for line in f if line.rstrip("\n") != ""]
m, n = len(grid), len(grid[0])
start_c = next(c for c,ch in enumerate(grid[0]) if ch == "S")
active = {start_c}
splits = 0

for r in range(0, m-1):
    next_active = set()
    for c in active:
        if grid[r+1][c] == "^":
            splits += 1
            if c-1 >= 0: next_active.add(c-1)
            if c+1 < n:  next_active.add(c+1)
        else:
            next_active.add(c)
    active = next_active
print(splits)
