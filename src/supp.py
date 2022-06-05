from time import sleep
from joblib import Memory, Parallel, delayed

memory = Memory(".cache", verbose=0)

b = 7


# @memory.cache
def longy(a: int):
    sleep(3)
    return a + b


print(list(Parallel(n_jobs=8)(delayed(longy)(i) for i in range(6))))
