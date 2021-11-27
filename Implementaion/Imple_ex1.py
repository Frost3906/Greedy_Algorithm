def solution():
  answer = ""
  n = int(input())
  plan = list(input().split())
  x,y = 1,1

  for i in plan :
    if i == 'U' :
      if y == 1 :
        continue
      else :
        y -= 1
    elif i == 'R' :
      if x == n :
        continue
      else :
        x += 1
    elif i == 'L' :
      if x == 1 :
        continue
      else :
        x -= 1
    elif i == 'D' :
      if y == n :
        continue
      else :
        y += 1

        
  answer = str(y)+" "+str(x)
  

  return answer
