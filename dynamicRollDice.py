import numpy as np

def dyRollDice(d, f, target):
    if target > f*d: return 0

    dp = np.zeros((d+1, target+1))

    dp[0][0] = 1

    for i in range(1, d + 1):
        for j in range(target + 1):
            for k in range(1, f + 1):
                if j-k < 0: continue
                dp[i][j] = dp[i][j] + dp[i-1][j-k]

    return dp

print(dyRollDice(3,4,8))
