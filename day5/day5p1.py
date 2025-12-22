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
    # print(merged)

    lc += 1
    queries = []
    while lc < len(lines):
        queries.append(int(lines[lc].strip()))
        lc += 1
    queries.sort()
    # print(queries)
    ans = 0
    pointer = 0
    for interval in merged:
        while pointer < len(queries) and queries[pointer] < interval[0]:
            pointer += 1
        # print(pointer)
        while pointer < len(queries) and queries[pointer] <= interval[1]:
            pointer += 1
            ans += 1
    print(ans)
