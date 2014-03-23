import numpy as np 
from mpmath import *
import math

def NPioverL(l,primeList,power,digits=100):
    mp.dps=digits
    return N(l,primeList,power)*(mp.pi**power)/(l**power)

def N(l,primeList,power):
    term=1
    sign=-1
    s=l**power
    f=open(primeList,'r')
    lines= f.readlines()
    f.close()
    for i in range(len(lines)):
        try:
            lines[i]=int(lines[i])
        except ValueError:
            lines.pop(i)
    while True:
        t=Nterm(l,lines,term,power)
        if t==0:
            break
        s+=t*sign
        sign*=(-1)
        term+=1
    return s



'''
def Nterm(l,primeList,term,power):
    primeIndices=range(term)
    return (l/product(primeIndices,primeList))**power

def product(primeIndices,primeList):
    p=1
    for e in primeIndices:
        p*=primeList[e]
    return p
'''

print NPioverL(100000000,'../million_primes.txt',3)