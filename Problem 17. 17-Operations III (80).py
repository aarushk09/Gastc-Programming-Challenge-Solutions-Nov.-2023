n = input().split()
n[0] = int(n[0])
n[2] = int(n[2])
if n[1] == "+":
  print(str(n[0] + n[2]))
elif n[1] == '-':
  print(str(n[0] - n[2]))
elif n[1] == '*':
  print(str(n[0] * n[2]))
elif n[1] == '/':
  div = n[0] / n[2]
  if n[0] % n[2] > .5:
    print(str(int(div) + 1))
  else:
    print(str(int(div)))