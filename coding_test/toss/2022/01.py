def solution(skills, team, k):
    answer = 0

    N = len(skills)
    min_t = min(team)
    max_t = max(team)

    s = 0

    skills_sum = sum(skills[s:s+k])

    while s + k - 1 <= N - 1:

        if s != 0:
            skills_sum -= skills[s-1]
            skills_sum += skills[s+k-1]

        tmp_sum = skills_sum

        if s <= min_t - 1 and s + k - 1 >= max_t - 1:
            tmp_sum *= 2

        if answer < tmp_sum:
            answer = tmp_sum
            

        s += 1


    return answer


print(solution([3,2,4,1], [2,4], 3))
print(solution([1,1,4,2,1,1], [2,1,5], 4))
print(solution([5,8,3,1], [4,3], 2))