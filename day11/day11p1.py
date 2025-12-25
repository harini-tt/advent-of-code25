with open('input.in', 'r') as file:
    lines = file.readlines()

g = {}
nodes = set()
for l in lines:
    line = l.strip()
    if not line or ":" not in line:
        continue
    u, rhs = line.split(":", 1)
    u = u.strip()
    vs = [v.strip() for v in rhs.strip().split() if v.strip()]
    g[u] = vs
    nodes.add(u)
    nodes.update(vs)
for v in nodes:
    g.setdefault(v, [])

print(g)

memo = {}
visiting = set()

def dfs(u):
    if u == 'out':
        return 1
    if u in memo:
        return memo[u]
    visiting.add(u)
    total = 0
    for v in g[u]:
        total += dfs(v)
    visiting.remove(u)
    memo[u] = total
    return total

print(dfs('you'))
