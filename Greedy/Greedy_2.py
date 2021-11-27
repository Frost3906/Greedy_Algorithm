# 숫자 카드 게임

def solution():
  answer = 0
  num_list = []
  n, m = map(int,input().split())

  for i in range(0,n):
    numbers = list(map(int,input().split()))
    num_list.append(min(numbers))

  answer = max(num_list)  
  return answer

