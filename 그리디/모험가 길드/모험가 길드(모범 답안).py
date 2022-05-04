import time
# time: 7.605552673339844e-05 => 0.00007초

n = int(input())
data = list(map(int, input().split()))
start_time = time.time()
data.sort()  # 항상 최소한의 모험가의 수만 포함하여 그룹을 결성할 수 있다.

result = 0  # 총 그룹의 수
cnt = 0  # 현재 그룹에 포함된 모험가의 수

for i in data:  # 공포도를 낮은 것부터 하나씩 확인하며
    cnt += 1  # 현재 그룹에 해당 모험가를 포함시키기
    if cnt >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1  # 총 그룹의 수 증가시키기
        cnt = 0  # 현재 그룹에 포함된 모험가의 수 초기화

print(result)  # 총 그룹의 수 출력
end_time = time.time()
print(f'time: {end_time - start_time}')
