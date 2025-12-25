import tqdm
from collections import deque

with open('input.in', 'r') as file:
    lines = file.readlines()

total = 0
for l in tqdm.tqdm(lines):
    parsed = l.strip().split()
    if not parsed:
        continue
    target = parsed[-1][1:-1]
    target = tuple(map(int, target.split(',')))
    k = len(target)

    deltas = []
    for button in parsed[1:-1]:
        inside = button[1:-1].strip()
        if inside == "":
            continue
        delta = [0] * k
        idxs = list(map(int, inside.split(',')))
        for idx in idxs:
            delta[idx] = 1
        deltas.append(tuple(delta))

    start = tuple(0 for _ in range(k))

    q = deque([start])
    dist = {start: 0}

    while q:
        state = q.popleft()
        cost = dist[state]

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
            if nxt not in dist:
                dist[nxt] = cost + 1
                q.append(nxt)

print(total)
