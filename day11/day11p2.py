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

def count_paths(g, start, target):
    memo = {}
    visiting = set()

    def dfs(u):
        if u == target:
            return 1
        if u in memo:
            return memo[u]
        if u in visiting:
            raise ValueError("Cycle detected (not a DAG).")
        visiting.add(u)
        total = 0
        for v in g.get(u, []):
            total += dfs(v)
        visiting.remove(u)
        memo[u] = total
        return total

    return dfs(start)

total = 0
# svr -> fft -> dac -> out
total += count_paths(g, 'svr', 'fft') * count_paths(g, 'fft', 'dac') * count_paths(g, 'dac', 'out')
# svr -> dac -> fft -> out
total += count_paths(g, 'svr', 'dac') * count_paths(g, 'dac', 'fft') * count_paths(g, 'fft', 'out')
print(total)