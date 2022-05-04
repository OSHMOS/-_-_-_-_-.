from itertools import combinations

L, C = map(int, input().split())
list = input().split()
list.sort()

contents = ['a', 'i', 'e', 'o', 'u']

for password in combinations(list, L):
    cnt = 0
    # if 'a' in x or 'i' in x or 'e' in x or 'o' in x or 'u' in x:
    for content in contents:
        if content in password:
            cnt += 1
    # if cnt >= 1 and cnt <= L - 2:
    if 1 <= cnt <= L - 2:
        print(''.join(password))
