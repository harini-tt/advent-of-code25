import heapq
with open('input.in', 'r') as file:
    lines = file.readlines()

def dist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2

boxes = []
for l in lines:
    x, y, z = l.strip().split(',')
    boxes.append((int(x), int(y), int(z)))
# print(boxes)

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        ri, rj = self.find(i), self.find(j)
        if ri == rj:
            return False
        if self.rank[ri] < self.rank[rj]:
            self.parent[ri] = rj
        elif self.rank[ri] > self.rank[rj]:
            self.parent[rj] = ri
        else:
            self.parent[rj] = ri
            self.rank[ri] += 1
        return True
    
heap = []

for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
        temp_dist = dist(boxes[i], boxes[j])
        heapq.heappush(heap, (dist(boxes[i], boxes[j]), i, j))

circuits = UnionFind(len(boxes))
for i in range(1000):
    _, x, y = heapq.heappop(heap)
    circuits.union(x, y)

sizes = {}
for i in range(len(boxes)):
    r = circuits.find(i)
    sizes[r] = sizes.get(r, 0) + 1

top3 = sorted(sizes.values(), reverse=True)[:3]
ans = top3[0] * top3[1] * top3[2]
print(ans)
