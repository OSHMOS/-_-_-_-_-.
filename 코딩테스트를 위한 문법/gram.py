n = 3
m = 4
# arr = [[0] * m] * 3
# 리스트 컴프리헨션이 2차원 리스트 초기화할 때 가장 정확한 방법이다.
arr = [[0] * m for _ in range(n)]
print(arr)

arr[1][1] = 5
print(arr)