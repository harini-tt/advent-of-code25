with open('input.in', 'r') as file:
    lines = file.readlines()
    ranges = lines[0].split(',')
    numbers = '-'.join(ranges).split('-')
    total = 0

    def check_divisor(n):
        n = str(n)
        length = len(n)
        for i in range(1, length):
            if length % i != 0:
                continue
            corr = n[:i] * (length // i)
            if n == corr:
                return True
        return False

    print(numbers)
    for i in range(0, len(numbers), 2):
        left, right = numbers[i], numbers[i+1]
        left_len = len(left)
        right_len = len(right)
        for number in range(int(left), int(right) + 1):
            if check_divisor(number):
                print(number)
                total += number
    print(total)


