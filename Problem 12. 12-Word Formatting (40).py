n, k = [int(x) for x in input().split()]
line = input().split()

i = 0
while i < len(line):
    remaining_space = k
    while i < len(line) and len(line[i]) <= remaining_space:
        print(line[i], end='')
        remaining_space -= len(line[i])
        i += 1

        if i < len(line) and len(line[i]) <= remaining_space:
            print('', end=' ')

    print("")
