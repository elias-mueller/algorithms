def sorted_subsets(self, A):
    """
    :param self:
    :param A: List of unique values
    :return: List of all subsets
    """
    def rec(A):
        if len(A) == 1:
            return [[A[0]]]
        s = [[A[0]]]
        t = rec(A[1:])
        for x in t:
            s.append(s[0] + x)
        return s + t

    if not A:
        return [[]]
    return [[]] + rec(sorted(A))
