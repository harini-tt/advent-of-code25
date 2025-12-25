curr = 50
count = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        rot = int(line[1:])
        count += rot // 100
        rot_eq = rot % 100
        if line[0] == 'L':
            if 0 < curr < rot_eq:
                count += 1
            curr = (curr - rot_eq) % 100
        else:
            if curr + rot_eq > 100:
                count += 1
            curr = (curr + rot_eq) % 100
        if curr == 0:
            count += 1

print(count)
