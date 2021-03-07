def alignment(s1, s2):
    """
    Return the best amount of points possible according to the following:
    -1 point if s1[k] != s2[k] : also if one is longer
    +1 point if s1[k] == s2[k]
    We can move letter around only if s1[k] and s2[k] != ' ' : no space at the same column

    :param s1: string
    :param s2: string
    :return: int
    """

    # Creating the array...
    # t[i][j] represents the best amount of point with s1[:i] and s2[:j]
    # Hence, the bottom right value is the best amount of point with full strings

    # 1. Fill in it with zero
    t = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]

    # 2. First line :
    # Take 0 charactere from s1 and x character from s2 for x in [0, len(s2)]
    # Thus, points are getting lower bc we are comparing x charactere with zero from s1
    t[0] = [x for x in range(0, -(len(s2)+1), -1)]

    # 3. Same principle for the first column
    for y in range(len(t)):
        t[y][0] = -y

    # Begin of the algorithm
    for y in range(1, len(s1)+1):
        for x in range(1, len(s2)+1):

            # Left score
            # Removing a letter => -1 point
            n1 = t[y][x-1] - 1

            # Up score
            # Removing a letter => -1 point
            n2 = t[y-1][x] - 1

            # Up left score
            n3 = t[y-1][x-1]
            # The two char could be equal => +1 point
            # Otherwise => -1 point
            if s1[y-1] == s2[x-1]:
                n3 += 1
            else:
                n3 -= 1

            # The score is the greater of the three
            t[y][x] = max(n1, n2, n3)

    # Returning the best amount of points
    return t[len(s1)][len(s2)]


points = alignment('abcd', 'eacd')
print(points)
