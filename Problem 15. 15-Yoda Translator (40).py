n = int(input())

for x in range(1, n+1):
  O_string = input()
  split_result = O_string.split(', ')
  split_1 = list(split_result[0])
  split_2 = list(split_result[1])
  split_2[0] = split_2[0].upper()
  split_2[-1] = ' '
  split_1[0] = split_1[0].lower()
  split_1.append('.')
  for x in split_2:
    print(x,end="")
  for x in split_1:
    print(x,end="")
  print()
 