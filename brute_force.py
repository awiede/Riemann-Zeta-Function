from decimal import *

def brute_force(s,n):
    getcontext().prec=64
    z=Decimal(0)
    for i in range(1,n+1):
        z+= Decimal(1)/Decimal(i)**s
    return z

print brute_force(3,1000000)

#n=10
'''
1.202007400659677610401237745009219693853295350713141455620407133
[Finished in 0.1s]
'''

#n=1,000,000
'''
1.202056903159094285899737911511449990848319625673748881792271222
[Finished in 97.8s]
'''

