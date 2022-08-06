def solution(M, load):
    answer = 0

    moved = [0] * len(load)

    for i in range(len(load)):
        if not moved[i]:

            tmp_sum = moved[i]

            for l in range(i+1, len(load)):
                if not moved[l]:
                    tmp_sum += moved[l]

                    

    return answer