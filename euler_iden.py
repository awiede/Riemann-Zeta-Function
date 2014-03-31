# \sum_{n=1}^{\infty} n^{-s} = \prod_p (1-p^{-s})^{-1}
from mpmath import *

def eu_iden(s, data,digits=100):
    mp.dps=digits
    primes = []
    with open(data) as inputfile:
        for line in inputfile:
            try:
                primes.append(int(line))
            except ValueError:
                pass
    prod=1
    for p in primes:
        prod*=(1-(1/mpf(p**s)))**(-1)
    inputfile.close()
    return prod

print eu_iden(5,'million_primes.txt')

#1 million primes
'''
1.202056903159594138313388959529919855966667293515320127109592847
[Finished in 374.1s]
'''

#10 primes
'''
1.201899271675867112763297039231311600287535772986512226898467185
[Finished in 1.7s]
'''