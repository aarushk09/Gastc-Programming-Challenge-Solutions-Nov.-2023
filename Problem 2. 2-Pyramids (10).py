n = int(input())
x = 1
for i in range(1,n+1):
  print(" " *((n-i)*2),end="")
  print("X " * (x-1),end="")
  print("X")
  x += 2