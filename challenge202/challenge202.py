def ExpressFactors(n):
    
    primeFactors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primeFactors.append(d)  
            n //= d
        d += 1
    if n > 1:
       primeFactors.append(n)
    print (*primeFactors, sep=" x ")

ExpressFactors(2)
ExpressFactors(4)
ExpressFactors(10)
ExpressFactors(60)