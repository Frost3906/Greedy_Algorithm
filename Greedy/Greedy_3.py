# 1이 될 때 까지

#내 구현
def solution():
  answer = 0
  n, k = map(int,input().split())

  while n != 1 :
    if n % k == 0 :
      n //= k
    else :
      n -= 1
    answer += 1
  

  return answer

#답안

def solution_() :
  n,k = map(int,input().split())
  answer = 0

  while True :
    target = (n // k) * k
    answer += (n - target)
    n = target
    if n < k:
      break
    answer += 1
    n //= k

  answer += (n -1)
  return answer  
