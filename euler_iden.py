# \sum_{n=1}^{\infty} n^{-s} = \prod_p (1-p^{-s})^{-1}
from decimal import *

def eu_iden(s, data='data.txt'):
    primes =open(data,'r')
    prod=1
    getcontext().prec=64
    for p in primes:
        p=Decimal(p)
        prod*=(Decimal(1)-(Decimal(1)/p**s))**(-1)
    primes.close()
    return prod

print eu_iden(3,'julia_billion_primes.txtgi')

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