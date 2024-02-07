def prime_factors(n):
  factors = []
  while n % 2 == 0:
    factors.append(2)
    n = n // 2
  i = 3
  while i * i <= n:
    while n % i == 0:
      factors.append(i)
      n = n // i
    i = i + 2
  if n > 2:
    factors.append(n)
  return factors

num = int(input(""))
factors = prime_factors(num)
for x in factors:
    print(x,end=" ")
