def algorithm4(problem, bestSeen = None, rowSplit = True, trace = None):
    # if it's empty, we're done 
    if problem.numRow <= 0 or problem.numCol <= 0:
        return None

    subproblems = []
    divider = []

    if rowSplit:
        # the recursive subproblem will involve half the number of rows
        mid = problem.numRow // 2

        # information about the two subproblems
        (subStartR1, subNumR1) = (0, mid)
        (subStartR2, subNumR2) = (mid + 1, problem.numRow - (mid + 1))
        (subStartC, subNumC) = (0, problem.numCol)

        subproblems.append((subStartR1, subStartC, subNumR1, subNumC))
        subproblems.append((subStartR2, subStartC, subNumR2, subNumC))

        # get a list of all locations in the dividing column
        divider = crossProduct([mid], range(problem.numCol))
    else:
        # the recursive subproblem will involve half the number of columns
        mid = problem.numCol // 2

        # information about the two subproblems
        (subStartR, subNumR) = (0, problem.numRow)
        (subStartC1, subNumC1) = (0, mid)
        (subStartC2, subNumC2) = (mid + 1, problem.numCol - (mid + 1))

        subproblems.append((subStartR, subStartC1, subNumR, subNumC1))
        subproblems.append((subStartR, subStartC2, subNumR, subNumC2))

        # get a list of all locations in the dividing column
        divider = crossProduct(range(problem.numRow), [mid])

    # find the maximum in the dividing row or column
    bestLoc = problem.getMaximum(divider, trace)
    neighbor = problem.getBetterNeighbor(bestLoc, trace)

    # update the best we've seen so far based on this new maximum
    if bestSeen is None or problem.get(neighbor) > problem.get(bestSeen):
        bestSeen = neighbor
        if not trace is None: trace.setBestSeen(bestSeen)

    # return when we know we've found a peak
    if neighbor == bestLoc and problem.get(bestLoc) >= problem.get(bestSeen):
        if not trace is None: trace.foundPeak(bestLoc)
        return bestLoc

    # figure out which subproblem contains the largest number we've seen so
    # far, and recurse, alternating between splitting on rows and splitting
    # on columns
    sub = problem.getSubproblemContaining(subproblems, bestSeen)
    newBest = sub.getLocationInSelf(problem, bestSeen)
    if not trace is None: trace.setProblemDimensions(sub)
    result = algorithm4(sub, newBest, not rowSplit, trace)
    return problem.getLocationInSelf(sub, result)

#Helper Method
def crossProduct(list1, list2):
    """
    Returns all pairs with one item from the first list and one item from 
    the second list.  (Cartesian product of the two lists.)

    The code is equivalent to the following list comprehension:
        return [(a, b) for a in list1 for b in list2]
    but for easier reading and analysis, we have included more explicit code.
    """

    answer = []
    for a in list1:
        for b in list2:
            answer.append ((a, b))
    return answer

arr = [
    [10, 9, 10, 9, 11, 66],
    [22, 12, 13, 11, 13, 55],
    [16, 7, 10, 13, 14, 44],
    [13, 21, 20, 23, 25, 17],
    [19, 33, 17, 18, 30, 19],
    [29, 24, 15, 20, 23, 33]
]
algorithm4(arr)