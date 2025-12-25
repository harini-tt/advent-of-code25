import numpy as np
with open('input.in', 'r') as file:
    def calculate_total(arr):
        w = max(len(s) for s in arr)
        arr = [s.ljust(w) for s in arr]
        out = []
        for col in range(w - 1, -1, -1):
            digits = [s[col] for s in arr if s[col] != ' ']
            if not digits:
                continue
            out.append(int(''.join(digits)))
        return out

    lines = [ln.rstrip('\n') for ln in file.readlines() if ln.rstrip('\n') != ""]
    W = max(len(ln) for ln in lines)
    grid = [list(ln.ljust(W)) for ln in lines]

    ops_row = grid.pop()
    digit_rows = grid
    is_sep = []
    for c in range(W):
        is_sep.append(
            ops_row[c] == ' ' and all(row[c] == ' ' for row in digit_rows)
        )
    blocks = []
    c = 0
    while c < W:
        while c < W and is_sep[c]:
            c += 1
        if c >= W:
            break
        start = c
        while c < W and not is_sep[c]:
            c += 1
        end = c
        blocks.append((start, end))

    ans = 0
    for start, end in blocks:
        op = next((ch for ch in ops_row[start:end] if ch in ('+', '*')), None)
        arr = [''.join(row[start:end]) for row in digit_rows]
        nums = calculate_total(arr)
        mid_ans = nums[0]
        for x in nums[1:]:
            if op == '*':
                mid_ans *= x
            else:
                mid_ans += x
        ans += mid_ans
    print(ans)
