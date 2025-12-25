with open('input.in', 'r') as file:
    lines = file.readlines()

def dist(a, b):
    return (abs(a[0] - b[0])+1) * (abs(a[1] - b[1])+1)

points = []
for l in lines:
    x, y = l.strip().split(',')
    points.append((int(x), int(y)))

print(points)
max_dist = -1
for i in range(len(points)):
    for j in range(i+1, len(points)):
        tmp_dist = dist(points[i], points[j])
        max_dist = max(max_dist, tmp_dist)

print(max_dist)
