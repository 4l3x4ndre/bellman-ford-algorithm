def alignement(s1, s2):
    """
    precondition : len(s1) == len(s2)
    :param s1:
    :param s2:
    :return:
    """
    # Keeping track of the longest string
    string_length = max(len(s1), len(s2))+1

    # Creating the array...
    # 1. Fill in it with zero
    t = [[0] * string_length for _ in range(string_length)]

    # 2. First line :
    # Take 0 charactere from s1 and x character from s2 for x in [0, len(s2)]
    # Thus, points are getting lower bc we are comparing x charactere with zero from s1
    t[0] = [x for x in range(0, -string_length, -1)]

    # Same principle for the first column
    for y in range(string_length):
        t[y][0] = -y

    # Begin of the algorithm
    for y in range(1, len(t)):

        for x in range(1, len(t)):



            # Left score
            # Removing a letter => -1
            n1 = t[y][x-1] - 1

            # Top score
            # Removing a letter => -1
            n2 = t[y-1][x] - 1

            # Top left score
            n3 = t[y-1][x-1]
            # The two character could be equal and we could gain 1 point
            # Otherwise we loose a point
            if s1[y-1] == s2[x-1]:
                n3 += 1
            else:
                n3 -= 1

            # The score is the greater from the three

            t[y][x] = max(n1, n2, n3)

    # returning the entire array (solution is at bottom right)
    return t


t = alignement('abcd', 'bcd')
for l in t:
    print(l)
