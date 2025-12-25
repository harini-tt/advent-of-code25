def find_best(number):
    # take 12 digit number
    best = -1
    for i in range(12):
        best = max(best, int(number[:i] + number[i+1:]))
    return str(best)

with open('input.in', 'r') as file:
    lines = file.readlines()
    ans = 0
    for l in lines:
        global_best = int(l[:12])
        for i in range(12, len(l)):
            global_best = max(global_best, int(find_best(str(global_best)) + l[i]))
        ans += global_best
    print(ans)
