with open('input.in', 'r') as file:
    lines = file.readlines()
    lc = 0
    intervals = []
    while lines[lc] != '\n':
        intervals.append(tuple(lines[lc].strip().split('-')))
        lc += 1
    for tup in range(len(intervals)):
        intervals[tup] = (int(intervals[tup][0]), int(intervals[tup][1]))
    # print(intervals)
    intervals = sorted(intervals)
    merged = [list(intervals[0])]
    for l, r in intervals[1:]:
        L, R = merged[-1]
        if l <= R:
            merged[-1][1] = max(R, r)
        else:
            merged.append([l, r])
    ans = 0
    for interval in merged:
        ans += interval[1] - interval[0] + 1
    print(ans)
