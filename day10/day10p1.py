with open('input.in', 'r') as file:
    lines = file.readlines()

def popcount(x):
    return x.bit_count()

total = 0
for l in lines:
    parsed = l.strip().split()
    diagram = parsed[0][1:-1]
    n_lights = len(diagram)
    b_mask = 0
    for i,ch in enumerate(diagram):
        if ch == '#':
            b_mask |= 1 << i
    # print(b_mask)
    buttons = []
    for button in parsed[1:-1]:
        pre_mask = button[1:-1]
        pre_mask = pre_mask.split(',')
        mask = 0
        for idx in pre_mask:
            mask |= 1 << int(idx)
        buttons.append(mask)
    # print(buttons)

    k = len(buttons)
    rows = []
    for j in range(n_lights):
        rowmask = 0
        for i, btn in enumerate(buttons):
            if (btn >> j) & 1:
                rowmask |= 1 << i
        rhs = (b_mask >> j) & 1
        rows.append(rowmask | (rhs << k))
    pivot_row_for_col = [-1] * k
    r = 0
    # elimination
    for col in range(k):
        pivot = -1
        for i in range(r, n_lights):
            if (rows[i] >> col) & 1:
                pivot = i
                break
        if pivot == -1:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        pivot_row_for_col[col] = r
        for i in range(n_lights):
            if i != r and ((rows[i] >> col) & 1):
                rows[i] ^= rows[r]
        r += 1
        if r == n_lights:
            break
    free_cols = [c for c in range(k) if pivot_row_for_col[c] == -1]
    free_mask = 0
    for c in free_cols:
        free_mask |= 1 << c
    pivot_cols = [c for c in range(k) if pivot_row_for_col[c] != -1]

    # brute force free vars
    f = len(free_cols)
    best = None
    for a in range(1 << f):
        x = 0
        # set free vars
        for t, col in enumerate(free_cols):
            if (a >> t) & 1:
                x |= 1 << col
        for col in pivot_cols[::-1]:
            prow = rows[pivot_row_for_col[col]]
            rhs = (prow >> k) & 1
            parity = popcount((prow & free_mask) & x) & 1
            val = rhs ^ parity
            if val:
                x |= 1 << col
            else:
                x &= ~(1 << col)

        presses = popcount(x)
        if best is None or presses < best:
            best = presses
    total += best
print(total)
