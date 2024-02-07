n = int(input())

for x in range(1, n+1):
  O_string = input()
  split_result = O_string.split(' ')
  for x in split_result:
    for y in x:
      if x[x.index(y)] == ',':
        index_of = split_result.index(x)
  word_comma = list(split_result[index_of])
  word_comma.remove(',')
  split_result[index_of] = ''.join(str(e) for e in word_comma)
  word_1 = list(split_result[0])
  word_1[0] = word_1[0].lower()
  word_1.append('.')
  word_last = list(split_result[-1])
  word_last[0] = word_last[0].upper()
  word_last.pop()
  split_result[0] = ''.join(str(e) for e in word_1)
  split_result[-1] = ''.join(str(e) for e in word_last)
  split_result = list(reversed(split_result))
  for x in range(0,len(split_result)):
    if x == index_of :
      print(split_result[index_of] + ', ',end="")
    else:
      print(split_result[x],end=' ')
  print()


