

def numRollsToTarget(d, f, target):
    if d == 0: 
        if target == 0: return 1
        else: return 0

    result = 0

    for x in range(f): 
        result = result + numRollsToTarget(d-1, f, target-(x+1))

    return result


print(numRollsToTarget(3, 4, 8))





