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
        self.size = [1] * size
    
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
            ri, rj = rj, ri
        self.parent[rj] = ri
        self.size[ri] += self.size[rj]
        if self.rank[ri] == self.rank[rj]:
            self.rank[ri] += 1
        return True
    
    def component_size(self, x):
        return self.size[self.find(x)]
    
heap = []

for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
        temp_dist = dist(boxes[i], boxes[j])
        heapq.heappush(heap, (dist(boxes[i], boxes[j]), i, j))

circuits = UnionFind(len(boxes))
last_i = last_j = None
while circuits.component_size(0) != len(boxes):
    _, x, y = heapq.heappop(heap)
    if circuits.union(x, y):
        last_i, last_j = x, y

ans = boxes[last_i][0] * boxes[last_j][0]
print(ans)
