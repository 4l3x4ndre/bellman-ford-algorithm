def alignement(s1, s2):

    # If one is empty, then score is negative according to the length of the other one
    if s1 == '' or s2 == '':
        return -1 * abs(len(s1) - len(s2))

    # If both of them is empty, then the recursion is over
    if s1 == '' and s2 == '':
        return 0

    # keep track of the longest string
    _s = s1
    if len(s2) > len(s1): _s = s2

    score1 = alignement('-' + s1[1:], s2[1:]) - 1
    score2 = alignement(s1[:1], '-' + s2[1:]) - 1
    score3 = alignement(s1[1:], s2[1:])

    if s1[0] == s2[0]:
        score3 += 1
    else:
        score3 -= 1

    return max(score1, score2, score3)


s = alignement('a', 'a')
print(s)
