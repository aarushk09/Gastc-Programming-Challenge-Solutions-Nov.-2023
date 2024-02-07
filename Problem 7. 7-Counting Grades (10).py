n = int(input())

a_count = 0
b_count = 0
c_count = 0
d_count = 0
f_count = 0

total = 0

for i in range(n):
  letter, percentage = input().split()
  percentage = int(percentage)

  if letter == 'A':
    a_count += 1
  elif letter == 'B':
    b_count += 1
  elif letter == 'C':
    c_count += 1
  elif letter == 'D':
    d_count += 1
  else:
    f_count += 1
  total += percentage

average = round(total / n, 2)

print(a_count)
print(b_count)
print(c_count)
print(d_count)
print(f_count)
print(average)
