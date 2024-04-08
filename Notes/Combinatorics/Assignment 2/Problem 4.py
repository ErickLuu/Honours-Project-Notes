from math import factorial as fc

def binom(n: int, k: int) -> int: return fc(n)/fc(k)/fc(n-k)

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
        count += (-1)**k * binom(n, k)* fc(2* n - k)* 2**k
    return count/2**n

def diffq5(n: int, k: int) -> int:
    return binom(n,2)**2 - k * n * (n-1)**2 + 2 * n * binom(k, 2) * (n-1) + n * k * (n * k - 2 * k + 1)/2 - 2 * n * binom(k, 2)*(k-1)

#print(diffq5(3, 2))
print(queue(2))