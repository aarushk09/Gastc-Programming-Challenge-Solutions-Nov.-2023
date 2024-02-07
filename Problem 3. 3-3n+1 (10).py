def cycle_length(n, count=0):
    if n == 1:
        return count
    elif n % 2 == 0:
        return cycle_length(n / 2, count + 1)
    else:
        return cycle_length(3 * n + 1, count + 1)

n = int(input(""))
print(cycle_length(n))
