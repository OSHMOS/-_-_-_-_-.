# 구구단
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f'{i} x {j} = {i * j}')
print('구구단 2~9단, 열단위 출력')
i = 1
while i <= 9:
    dan = 2
    while dan <= 9:
        print(f'{dan} x {i} = {dan * i:2}', end=" ")
        dan += 1
    print()
    i += 1

# 실수면 f, 정수면 d, 문자열이면 s
# 왼쪽 정렬은 특수 기호 X, 가운데 정렬은 특수 기호 ^, 오른쪽 정렬은 특수 기호 >
# 자릿 수 맞추기는 :(맞추고 싶은 자릿 수)
