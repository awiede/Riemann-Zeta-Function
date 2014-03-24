function primes(n)
    primes=zeros(Int,n)
    primes[1]=2
    i=3
    counter=2
    while primes[n]==0
        for num in primes
            if num >= ifloor(sqrt(i)+1) || num==0
                primes[counter] = i
                counter += 1
                i += 1
                break
            elseif (i % num)==0
                break
            end
        i += 1
        end
    end
    return primes
end

function NPioverL(l,primeList,power)
    return N(l,primeList,power)*(pi^power)/(l^power)
end

function N(l,primeList,power)
    term=1
    sign=-1
    sum=l^power
    numbers=readdlm(primeList,Int)
    while true
        t=Nterm(l,numbers,term,power)
        if t==0
            break
        end
        sum+=t*sign
        sign*=-1
        term+=1
    end
    return sum
end

function Nterm(l,primeList,term,power)
    primeIndices=zeros(term)
    return NtermRecursive(l,primeIndices,primeList,power)
end

function NtermRecursive(l,primeIndices,primeList,power)
    i=1
    while i<length(primeIndices) && primeIndices[i]!=0
        i+=1
    end
    if i==length(primeIndices)
        p=1
        for e in primeIndices
            if e!=0
                p*=primeList[e]
            end
        end
        return ifloor(l/p)^power
    end
    sum=0
    while true
        primeIndices[i]=primeIndices[i]+1
        if i==1 && primeIndices[i]==length(primeList)
            print("Need more primes")
            break
        elseif i>1 && primeIndices[i]>primeIndices[i-1]
            break
        end
        p=1
        for j=1:i
            p*=int(primeList[primeIndices[j]])
        end
        if p>l
            break
        end
        sum+=NtermRecursive(l,primeIndices,primeList,power)
    end
    return sum
end

function product(primeIndices,primeList)
    p=1
    for i=1:length(primeIndices)
        p*=primeList[primeIndices[i]+1]
    end
    return p
end

function N2term(l,pl)
    i=0
    sum=0
    while true
        if i>=length(pl)
            print("Need more primes")
            break
        elseif l<pl[i]
            break
        end
        sum+=floor(l/pl[i])^2
        i+=1
    end
    return sum
end
