import numpy as np
from math import factorial as fc

def queue(n: int) -> int:
    '''
    Queue function looks at n (completely identical) twins 
    and counts the number of ways to arrange them such that no two twins sits next to each other.
    Note that Python may hit rounding errors for large numbers.
    '''
    count = 0
    for k in range(n + 1):
        '''
        Count is from 0 to n inclusive. Calculates values from paper.
        '''
        count += (-1)**k * fc(n) * fc(2* n - k)* 2**k /fc(k)/fc(n-k)
    return count/2**n
print(queue(4))