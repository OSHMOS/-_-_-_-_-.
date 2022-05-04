import time
# time : 8.58306884765625e-05 => 0.00008초

N = int(input())  # 모험가의 수
data = list(map(int, input().split()))

start_time = time.time()
cnt = 0

for i in range(len(data)):
    if data[i] > data[i - 1]:
        N -= data[i]
        cnt += 1
    if N >= data[i-1]:
        N -= data[i-1]
        cnt += 1
    if N <= 0:
        break

print(cnt)

end_time = time.time()
print(f'time : {end_time - start_time}')
