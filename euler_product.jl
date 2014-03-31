function euler(s,data="million_primes.txt")
    primes = readcsv(data)
    prod=1
    for p in primes
        prod*=(1)/(1-(1/BigFloat(p^s)))
    end
    return prod
end

#julia> euler(3, "julia_billion_primes.txt")
#no method /(Int64,RepString)
