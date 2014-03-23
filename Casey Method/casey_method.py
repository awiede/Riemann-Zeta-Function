import numpy as np 
from mpmath import *
import math

def NPioverL(l,primeList,power,digits=100):
    mp.dps=digits
    mp.prec+=203
    return N(l,primeList,power)*(mp.pi**power)/l**power

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

def Nterm(l,primeList,term,power):
    primeIndices=[-1]*term
    return NtermRecursive(l,primeIndices,primeList,power)

def NtermRecursive(l, primeIndices, primeList, power):
    i=0
    #print "len(primeIndices)",len(primeIndices)
    #print "primeIndices[i]!=-1",primeIndices[i]!=-1
    while i<len(primeIndices) and primeIndices[i]!=-1:
        i+=1
    if i==len(primeIndices):
        p=1
        for e in primeIndices:
            p*=primeList[e]
        #print "p",p
        return int(l/p)**power

    sigma=0
    while True:
        primeIndices[i]=primeIndices[i]+1
        #print "len(primeList)",len(primeList)
        if i==0 and primeIndices[i]==len(primeList):
            print "Need more primes"
            break
        #print "primeIndices[i]>primeIndices[i-1]",primeIndices[i]>primeIndices[i-1]
        if i>0 and primeIndices[i]>primeIndices[i-1]:
            break
        p=1
        for j in xrange(i+1):
            p*=int(primeList[primeIndices[j]])
        if p>l:
            break
        sigma+=NtermRecursive(l,copyList(primeIndices),primeList,power)
        #print sigma
    return sigma

def copyList(oldlst):
    newlst=[]
    for i in range(len(oldlst)):
        newlst=newlst+[oldlst[i]]
    return newlst

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

print NPioverL(10**4,'../million_primes.txt',2)



