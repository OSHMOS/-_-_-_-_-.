# 끝까지 나눌 필요가 없다.
# 제곱근까지만 나누면 된다. -> 제곱근 함수 sqrt() import math
import math

# 소수 판별 함수


def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x) + 1)):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임
