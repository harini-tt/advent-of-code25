with open('input.in', 'r') as file:
    lines = file.readlines()
    ranges = lines[0].split(',')
    numbers = '-'.join(ranges).split('-')
    total = 0

    def check_if_double( n):
        n = str(n)
        length = len(n)
        if length % 2 != 0:
            return False
        half = length / 2
        return n[:length//2] == n[length//2:]



    print(numbers)
    for i in range(0, len(numbers), 2):
        left, right = numbers[i], numbers[i+1]
        left_len = len(left)
        right_len = len(right)
        # n = left_len if (left_len % 2 == 0) else right_len
        # print(left, right)
        # print(n)
        # if n % 4 != 0:
        #     continue
        # divisor = 10 ** (n//2) + 1 
        # print(divisor)
        for number in range(int(left), int(right) + 1):
            if check_if_double(number):
                total += number
            # if number % divisor == 0:
            #     total += number
    print(total)


