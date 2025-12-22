with open('input.in', 'r') as file:
    lines = file.readlines()
    ans = 0
    for l in lines:
        l = l.strip()
        best_first = int(l[0])
        best = -1
        for c in l[1:]:
            d = int(c)
            best = max(best, best_first * 10 + d)
            best_first = max(best_first, d)
        ans += best
    print(ans)
