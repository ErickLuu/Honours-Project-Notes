import numpy as np
from math import factorial as fc

def queue(n: int) -> int:
    count = 0
    for k in range(n + 1):
        count += (-1)**k * fc(n) * fc(2* n - k)* 2**k /fc(k)/fc(n-k)
    return count/2**n
print(queue(4))