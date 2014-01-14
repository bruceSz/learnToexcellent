class PrimeSieve
    constructor: (@max)->
        @nums = [2..@max]
        for p in @nums
            d = 2*p
            while p!=0 and d<=@max
                @nums[d-2]=0
                d+=p
    isPrime: (n)->@nums[n-2]!=0
    thePrimes: ->@nums.filter (n)-> n!=0


class CircularPrimeGenerator extends PrimeSieve
    genPerms = (num)->
        s = new String num
        x = (for i in[0...s.length]
            s[i+1...s.length].concat s[0..i])
        x.map (a)->parseInt(a)

    isCircularPrime: (n)->
        perms = genPerms(n)
        len = perms.length
        primePerms = perms.filter (p)=>@isPrime(p)
        len ==primePerms.length
    theCircularPrimes:->
        (p for p in @thePrimes() when @isCircularPrime(p))


max = process.argv[2]
generator = new CircularPrimeGenerator max

console.log "Number of circular primes less than #{max} is
#{generator.theCircularPrimes().length}"
