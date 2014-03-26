#to use:
#first, get a list of primes.
#for example, primeList=p.primelist(1000000)
#
#second, call NPioverL on various large values of l
#for example, NPioverL(100000,primeList,2)

import csv
import math
from mpmath import *

def primelist(max):
    pl=[2]
    i=3
    while(i<max):
        j=2
        while(j<=math.sqrt(i)):
            if (i%j==0):
                break
            j=j+1
        if j>math.sqrt(i):
            pl=pl+[i]
        i=i+2
    return pl

def NPioverL(l,primeList,power,digits=1000):
    mp.dps=digits
    return N(l,primeList,power)*(mp.pi**power)/(l**power)

def N(l,primeList,power):
    term=1
    sign=-1
    sum=l**power
    while True:
        t=Nterm(l,primeList,term,power)
        if t==0:
            break
        sum=sum+t*sign
        sign=sign*(-1)
        term=term+1
    return sum

def Nterm(l,primeList,term,power):
    primeIndices=[-1]*term
    return NtermRecursive(l,primeIndices,primeList,power)

def NtermRecursive(l,primeIndices,primeList,power):
    i=0
    while i<len(primeIndices) and primeIndices[i]!=-1:
        i=i+1

    if i==len(primeIndices):
        return (math.floor(l/product(primeIndices,primeList)))**power

    sum=0
    while True:
        primeIndices[i]=primeIndices[i]+1
        if i==0 and primeIndices[i]==len(primeList):
            print "Need more primes"
            break
        if i>0 and primeIndices[i]>=primeIndices[i-1]:
            break
        
        if product(primeIndices[:i+1],primeList)>l:
            break
        sum=sum+NtermRecursive(l,copyList(primeIndices),primeList,power)
    return sum

def product(primeIndices,primeList):
    p=1
    for i in range(len(primeIndices)):
        p=p*primeList[primeIndices[i]]
    return p

def copyList(oldlst):
    newlst=[]
    for i in range(len(oldlst)):
        newlst=newlst+[oldlst[i]]
    return newlst

#this is just for verification
def N2term2(l,pl):
    i=0
    sum=0
    while True:
        if i>=len(pl):
            print "Need more primes"
            break
        if l<pl[i]:
            break
        sum=sum+math.floor(l/pl[i])**2
        i=i+1
    return sum

results = []
#filename='../million_primes.txt'
filename='../../Zeta Function/julia_10billion_primes.txt'
with open(filename) as inputfile:
    for line in inputfile:
        try:
            results.append(int(line))
        except ValueError:
            pass

computation= NPioverL(10**6,results, 3)
#computation= NPioverL(10**5,results, 3)
print computation
#writefile=open('testwritefile.txt','w')
#writefile= open('../../Zeta Function/10billion_result.txt','w')

writefile.write('NPioverL(l=10**6,10bil primes, 3)\n'+str(computation))
writefile.close()

'''
Computation with 1 billion primes, l=10**4
6.000223133456999256406429341372316118630134313659210561498714093401657145976757325913407670276406751
[Finished in 57.0s]

z(3)
1b primes, l=10**4
25.7946348142317005689130286067437538366171646585455991960556469767637520430255693554896049449805637
[Finished in 57.7s]
'''