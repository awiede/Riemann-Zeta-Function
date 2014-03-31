function ramanujan(k)
    sigma = zeros(BigFloat,k)

    for i=1:k #inclusive on both sides
        sigma[i]=BigFloat(((1/2)^i)*(1/i^3))
        end
        diff1=BigFloat((4/21)*log(2)^3)
        diff2=BigFloat(2/21)*BigFloat(pi^2)*BigFloat(log(2))
        result=BigFloat(8/7)*BigFloat(sum(sigma)) - diff1 + diff2
        return result
    end
