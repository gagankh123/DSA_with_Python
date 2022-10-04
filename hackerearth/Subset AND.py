t = int(input())
for tc in range(t):
  (z,n) = map(int, input().split(' '))
  s = list(map(int, input().strip().split(' ')))[:n]
  flag = 0
  for i in s:
    z = z & i
    if z == 0:
      flag = 1
      break
  if flag == 1:
    print("Yes")
  else:
    print("No")