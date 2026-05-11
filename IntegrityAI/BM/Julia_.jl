function my_fac(N::int)
    for i in 1:isqrt(N)
        t = BigInt(i)
        if N != 1 && N%t !=0
            break
        N/=t
    end
    if N ==1
        return i
    else
        return 0
    end
end

function faquare(M)
    result =[]
    for N=1:M 
        ans = []
        for b=1:isqrt(M)
            if my_fac(BigInt(b)^2 -N) == true
                push!(ans,(my_fac2(igInt(b)^2 -N),b))
            end
        end
        if length(ans) >= 3
            push!(result, (N,ans))
        end
    end
    return result
