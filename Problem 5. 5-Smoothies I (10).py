vk = input().split(' ')
volume = int(vk[0])
friends = int(vk[1])

for x in range(friends):
  friend_volume = int(input())
  volume -= friend_volume

print(volume)