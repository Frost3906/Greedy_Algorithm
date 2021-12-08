#게임 개발

# 문제에 대한 이해가 잘 되지 않았다.
# 정확히는 좌표 파악을 이상하게 했었다. 그래서 시간이 초과되었다.
# 결국 입력 받기 -> 지도 생성 -> 이동로직 구현 순으로 해나가면 된다?

def solution() :
    answer = 1
    #지도 크기
    n,m = map(int,input().split())
    #초기위치, 방향
    x,y,d = map(int, input().split())

    land = []
    chk_land = []
    #지도 정보 생성
    for i in range(m):
        row = list(map(int,input().split()))
        land.append(row)
        chk_land.append(row)

    #이동 로직
    while True:
        land[x][y] = 2

        if d == 0 :
            if (land[x][y-1] == 2 or land[x][y-1] == 1) and (land[x][y+1] == 2 or land[x][y+1] == 1) and (land[x-1][y] == 2 or land[x-1][y] == 1):
                x += 1
                if land[x][y] == 1:
                    break
                elif land[x][y] == 0:
                    answer += 1
                    continue
            elif land[x][y-1] == 0:
                d = 3
                y -= 1
                land[x][y] = 2
                answer += 1
                continue
            else :
                d = 3
                continue

        elif d == 1 :
            if (land[x][y+1] == 2 or land[x][y+1] == 1) and (land[x-1][y] == 2 or land[x-1][y] == 1) and (land[x+1][y] == 2 or land[x+1][y] == 1):
                y -= 1
                if land[x][y] == 1:
                    break
                elif land[x][y] == 0:
                    answer += 1
                    continue
            elif land[x-1][y] == 0:
                d = 0
                x -= 1
                land[x][y] = 2
                answer += 1
                continue
            else :
                d = 0
                continue

        elif d == 2 :
            if (land[x][y+1] == 2 or land[x][y+1] == 1) and (land[x][y-1] == 2 or land[x][y-1] == 1) and (land[x+1][y] == 2 or land[x+1][y] == 1):
                x -= 1
                if land[x][y] == 1:
                    break
                elif land[x][y] == 0 :
                    answer += 1
                    continue
            elif land[x][y+1] == 0:
                d = 1
                y += 1
                land[x][y] = 2
                answer += 1
                continue
            else :
                d = 1
                continue

        elif d == 3 :
            if (land[x+1][y] == 2 or land[x+1][y] == 1) and (land[x-1][y] == 2 or land[x-1][y] == 1) and (land[x][y-1] == 2 or land[x][y-1] == 1):
                y += 1
                if land[x][y] == 1:
                    break
                elif land[x][y] == 0: 
                    answer += 1
                    continue
            elif land[x+1][y] == 0:
                d = 2
                x += 1
                land[x][y] = 2
                answer += 1
                continue
            else :
                d = 2
                continue
    return answer
