import itertools

L, C = map(int, input().split())
# pw_data = str(input().split())
pw_data = list(input().split())

cnt = 0

for x in itertools.combinations(pw_data, 4):
    if 'a' in x or 'i' in x or 'e' in x or 'o' in x or 'u' in x:
        pw_list = sorted(list(x))
        pw_result = ''.join(pw_list)
        cnt += 1
    print(pw_result, cnt)
