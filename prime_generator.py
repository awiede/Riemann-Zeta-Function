import numpy as np
import pandas as pd


def prime_numbers(n):
    primes=np.zeros_like(np.arange(n))
    primes[0]=2
    i=3
    counter=1
    while primes[-1]==0:
        for num in primes:
            if num>(int(np.sqrt(i))+1) or num==0:
                primes[counter]=i
                counter+=1
                i+=1
                break
            elif (i%num)==0:
                break
        i+=1
    numbers=pd.DataFrame(primes, index=np.arange(1,n+1), columns=['Primes'])
    numbers.to_csv('data.txt',header=False ,index=False)
    return numbers

print prime_numbers(10)

'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 1000000 entries, 1 to 1000000
Data columns:
Primes    1000000  non-null values
dtypes: int64(1)
[Finished in 25765.2s]

7.157 hours
''' 