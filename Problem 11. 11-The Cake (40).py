def count_obtuse_candles(N, data):
    result = []
    for i in range(N):
        n, x, z = data[i]
        count = (z - x + n - 1) % n
        result.append(count)
    return result

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

result = count_obtuse_candles(N, data)

for count in result:
    print(count)
