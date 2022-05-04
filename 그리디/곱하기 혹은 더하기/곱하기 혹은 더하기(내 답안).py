import time

S = list(input())
start_time = time.time()
result = 1

for i in range(len(S)):
    if S[i] == '0':
        S[i] = 1
    result *= int(S[i])

print(result)

end_time = time.time()
print(f'time: {end_time - start_time}')
