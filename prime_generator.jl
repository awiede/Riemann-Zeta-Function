function prime_numbers(n)
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


function writePrimes(n)
    f=open("data.txt","w")
    tic()
    println(f,primes(n))
    toc()
    close(f)
end
