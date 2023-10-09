import math


def solution(n):
    answer = []

    d = 2
    sqrt = int(math.sqrt(n))

    while d <= sqrt:
        if n % d != 0:
            d += 1
        else:
            answer.append(d)
            n //= d

    if n > 1:
        answer.append(n)

    return sorted(list(set(answer)))

