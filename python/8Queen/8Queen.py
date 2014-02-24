import random
def confilct(state,nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0, nextY-i):
            return True
    return False

def queens(num=8, state=()):
    for pos in range(num):
        if not confilct(state, pos):
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result

def prettyprint(solution):
    for pos in solution:
        print '.' * pos +'X' +'.' * (len(solution)-pos-1)
        
prettyprint(random.choice(list(queens(8))))
