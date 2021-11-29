# 왕실의 나이트
# 20분
# 8 * 8
#My solution
# It is work, but like a bullshit
def solution() :
  answer = 0
  alph_list = ['a','b','c','d','e','f','g','h']
  num_list = [1,2,3,4,5,6,7,8]
  knight_loc = list(str(input()))
  for i in range(len(alph_list)):
    knight_loc[0] = knight_loc[0].replace(alph_list[i], str(num_list[i]))

  point = []
  point.append(str(int(knight_loc[0])+2)
               +str(int(knight_loc[1])+1))
  point.append(str(int(knight_loc[0])+2)
               +str(int(knight_loc[1])-1))
  point.append(str(int(knight_loc[0])+1)
               +str(int(knight_loc[1])+2))
  point.append(str(int(knight_loc[0])-1)
               +str(int(knight_loc[1])+2))
  point.append(str(int(knight_loc[0])-2)
               +str(int(knight_loc[1])+1))
  point.append(str(int(knight_loc[0])-2)
               +str(int(knight_loc[1])-1))
  point.append(str(int(knight_loc[0])+1)
               +str(int(knight_loc[1])-2))
  point.append(str(int(knight_loc[0])-1)
               +str(int(knight_loc[1])-2))

  for i in point :
    if not ('-' in i) and not ('0' in i) and not ('9' in i):
      answer += 1
  
  return answer

#Book answer
def solution_():
  pass