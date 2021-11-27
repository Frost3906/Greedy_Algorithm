
# 큰 수의 법칙 
# - 반복문
def solution(first_line, second_line):
  answer = 0
  cnts = list(map(int,first_line.split()))
  numbers = list(map(int,second_line.split()))
  numbers.sort(reverse = True)
  
  first_number = numbers[0]
  second_number = 0
  
  if cnts[0] > 1:
    second_number = numbers[1]

  cnt = 0
  for i in range(0,cnts[1]):
    if cnt == cnts[2] :
      answer += second_number
      cnt = 0
      continue

    answer += first_number
    cnt += 1
  
  return answer

#반복문 X
def solution_(first_line, second_line):
  answer = 0
  n,m,k = map(int,first_line.split())
  numbers = list(map(int,second_line.split()))

  numbers.sort()
  first_num = numbers[n-1]
  second_num = numbers[n-2]

  cnt = int(m / (k +1) ) * k
  cnt += m % (k+1)
  
  
  answer += cnt * first_num
  answer += (m - cnt) * second_num
    
    
  return answer


  