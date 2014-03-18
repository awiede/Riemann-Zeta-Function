#z(3) = (8/7) sigma_{k=1} (1/2)^k (1/k^3) - (4/21)log(2)^3 + (2/21)pi^2 log(2)
import numpy as np
from math import log
from mpmath import *
mp.prec+=203

def ramanujan(k):
    k=mpf(k)
    array=np.zeros_like(np.arange(k))
    for i in np.arange(1,k+1):
        array[i-1]=(mpf(0.5)**mpf(i))*(mpf(1)/mpf(i)**mpf(3))
    diff1=(mpf(4)/mpf(21))*mpf(np.log(2))**(mpf(3))
    diff2=(mpf(2)/mpf(21))*mpf(np.pi)**mpf(2)*mpf(np.log(2))
    sigma=mpf(8)/mpf(7)*np.sum(array) -diff1 + diff2
    return sigma

print ramanujan(1000)

'''
ramanujan(100000)
1.202056903159594 219172697056127964443040446908761972497151039299
1.202056903159594 219172697056127964443040446908761972497151039299338668132465
1.202056903159594 199262084435399337312783641011903338754877017697188092024191347e+00
1.202056903159594 167907395920706195748042532412243488898016705349787436569040695e+00
[Finished in 52.3s]
'''
mp.prec-=203