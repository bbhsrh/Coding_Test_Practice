
def solution(s):
    # answer = 0
    s = s.split(' ')
    answer = []
    for i in s:
        # print(id, i)
        if (i == 'Z'):

            # answer.pop()
            answer.pop()
        else:
            answer.append(i)

    answer = list(map(int, answer))
    print(answer)
    return sum(answer)
