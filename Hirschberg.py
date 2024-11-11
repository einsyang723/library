import numpy as np # type: ignore

def Ins(X):
    return -2

def Del(X):
    return -2

def Sub(X, Y):
    if (X == Y):
        return 2
    else:
        return -1 

def NeedlemanWunsch(X, Y, match=1, mismatch=-1, gap=-1):
    # 初始化矩陣
    m = len(X)
    n = len(Y)
    score_matrix = [[0 for j in range(n + 1)] for i in range(m + 1)]
    traceback_matrix = [['' for j in range(n + 1)] for i in range(m + 1)]

    # 初始化第一行和第一列 (插入 gap penalties)
    for i in range(1, m + 1):
        score_matrix[i][0] = gap * i
        traceback_matrix[i][0] = 'U'  # Up, meaning a gap in Y

    for j in range(1, n + 1):
        score_matrix[0][j] = gap * j
        traceback_matrix[0][j] = 'L'  # Left, meaning a gap in X

    # 填充矩陣
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                score = match
            else:
                score = mismatch

            diag_score = score_matrix[i - 1][j - 1] + score  # 來自左上方 (匹配/不匹配)
            up_score = score_matrix[i - 1][j] + gap          # 來自上方 (插入 gap)
            left_score = score_matrix[i][j - 1] + gap        # 來自左方 (插入 gap)

            # 選擇最高得分並記錄追溯路徑
            score_matrix[i][j] = max(diag_score, up_score, left_score)

            if score_matrix[i][j] == diag_score:
                traceback_matrix[i][j] = 'D'  # Diagonal, meaning match/mismatch
            elif score_matrix[i][j] == up_score:
                traceback_matrix[i][j] = 'U'  # Up, meaning gap in Y
            else:
                traceback_matrix[i][j] = 'L'  # Left, meaning gap in X

    # 追溯以獲得最佳對齊
    aligned_X = ""
    aligned_Y = ""
    i = m
    j = n

    while (i > 0 or j > 0):
        if traceback_matrix[i][j] == 'D':
            aligned_X = X[i - 1] + aligned_X
            aligned_Y = Y[j - 1] + aligned_Y
            i -= 1
            j -= 1
        elif traceback_matrix[i][j] == 'U':
            aligned_X = X[i - 1] + aligned_X
            aligned_Y = '-' + aligned_Y
            i -= 1
        else:  # traceback_matrix[i][j] == 'L'
            aligned_X = '-' + aligned_X
            aligned_Y = Y[j - 1] + aligned_Y
            j -= 1

    return aligned_X, aligned_Y

def NWScore(X, Y):
    # 2 * (length(Y) + 1) array
    Score =  [[0] * (len(Y) + 1) for _ in range(2)]
    Score[0][0] = 0 
    for j in range(1, len(Y)+1):
        Score[0][j] = Score[0][j-1] + Ins(Y[j-1]) #Ins(Y) means inserting Y
    for i in range(1, len(X)+1): # Init array
        Score[1][0] = Score[0][0]+Del(X[i-1]) #Del(X) means deleting X
        for j in range(1, len(Y)+1):
            scoreSub = Score[0][j-1] + Sub(X[i-1], Y[j-1]) #Sub(X, Y) means replacing X with Y
            scoreDel = Score[0][j] + Del(X[i-1])
            scoreIns = Score[1][j-1] + Ins(Y[j-1])
            Score[1][j] = max(scoreSub, scoreDel, scoreIns)
        # Copy Score[1] to Score[0]
        Score[0][:] = Score[1][:]
    # LastLine = [0*len(Y)] 
    LastLine = Score[0]
    print('LastLine:', LastLine)
    return LastLine

def Hirschberg(X, Y):
    Z = ""
    W = ""
    if (len(X) == 0):
        for i in range(len(Y)):
            Z = Z + '-'
            W = W + Y[i]
    elif (len(Y) == 0):
        for i in range(len(X)):
            Z = Z + X[i]
            W = W + '-'
    elif (len(X) == 1 or len(Y) == 1):
        (Z, W) = NeedlemanWunsch(X, Y)
    else:
        xlen = len(X)
        xmid = len(X) // 2
        ylen = len(Y)

        ScoreL = NWScore(X[:xmid], Y)
        ScoreR = NWScore(X[xmid+1:][::-1], Y[::-1])
        combined_score = [ScoreL[i] + ScoreR[ylen - i - 1] for i in range(ylen + 1)]
        ymid = np.argmax(combined_score)

        # (Z,W) = Hirschberg(X[1:xmid], Y[1:ymid]) + Hirschberg(X[1:xlen], Y[1:ylen])
        (Z_left, W_left) = Hirschberg(X[:xmid], Y[:ymid])
        (Z_right, W_right) = Hirschberg(X[xmid:], Y[ymid:])

        Z = Z_left + Z_right
        W = W_left + W_right
    print('progress:', Z, W)
    return (Z, W)

print(Hirschberg('AGTACGCA', 'TATGC'))