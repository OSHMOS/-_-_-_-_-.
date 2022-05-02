def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


print(is_prime_number(4))
print(is_prime_number(7))
# 굉장히 비효율적인 코드 -> 시간복잡도가 O(X)이기 때문이다.
