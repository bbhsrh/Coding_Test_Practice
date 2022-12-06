def solution(dots):
    answer = 1

    for i in range(1, 4):
        if dots[i][0] == dots[0][0]:
            print(dots[i][0])
            answer *= (dots[i][1] - dots[0][1])
        if dots[i][1] == dots[0][1]:
            # print(i)
            answer *= (dots[i][0] - dots[0][0])

        # print(dots[i])
    # print()
    return abs(answer)