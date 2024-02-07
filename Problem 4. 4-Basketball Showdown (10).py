score = list(input())
ascore = 0
jscore = 0
win = ""
i = 0
i2 = 0
for x in score:
  try:
    score[i2] = int(x)
  except:
    pass
  i2 += 1
for x in score:
  if x == 'A':
    ascore += score[i+1]
  elif x == 'J':
    jscore += score[i+1]
  if ascore >= 11 or jscore >= 11:
    if (ascore - jscore >= 2):
      win = "Abby"
      break
    elif (jscore - ascore >= 2):
      win = "John"
      break
  i += 1
print(win)