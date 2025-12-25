import heapq
import tqdm
with open('input.in', 'r') as file:
    lines = file.readlines()

total = 0
for l in tqdm.tqdm(lines):
    parsed = l.strip().split()
    target = parsed[-1][1:-1]
    target = list(map(int, target.split(',')))
    target = tuple(target)
    k = len(target)
    # print(target)

    deltas = []
    for button in parsed[1:-1]:
        delta = [0] * k
        idxs = list(map(int, button[1:-1].split(',')))
        for idx in idxs:
            delta[idx] = 1
        deltas.append(tuple(delta))
    # print(deltas)

    start = tuple(0 for _ in range(k))
    # dijkstra
    pq = [(0, start)]
    best = {start: 0}
    while pq:
        cost, state = heapq.heappop(pq)
        if cost != best.get(state, None):
            continue
        if state == target:
            total += cost
            break
        for delta in deltas:
            nxt = []
            ok = True
            for s, inc, t in zip(state, delta, target):
                v = s + inc
                if v > t:
                    ok = False
                    break
                nxt.append(v)
            if not ok:
                continue
            nxt = tuple(nxt)
            ncost = cost + 1
            if ncost < best.get(nxt, 10**30):
                best[nxt] = ncost
                heapq.heappush(pq, (ncost, nxt))
print(total)
