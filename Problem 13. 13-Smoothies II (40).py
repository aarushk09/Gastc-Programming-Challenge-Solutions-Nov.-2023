ik = input().split(' ')
ingredients = int(ik[0])
friends = int(ik[1])
volume = 0

for x in range(ingredients):
  information = input().split(' ')
  type = information[0]
  if type == "sphere":
    volume += (4/3) * (float(information[1])**3) * 3.14
  if type == "cube":
    volume += float(information[1])**3
  if type == "cylinder":
    volume += 3.14 * (float(information[1])**2) * float(information[2])
  if type == "cone":
    volume += (3.14 * (float(information[1])**2) * float(information[2]))/3
  
print(int(volume // friends))