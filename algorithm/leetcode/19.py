class Solution:
    def canCompleteCircuit(self,gas,cost):
        
        length = len(gas)
        if length ==0:
            return -1
        
        #costSum = 0
        #gasSum = 0

        #for i in xrange(0,length):
        #    costSum += cost[i]
        #    gasSum +=gas[i]
        #if costSum > gasSum:
        #    return -1

        currentGas = 0
        pos = length-1
        #for i in xrange(0,length):
        i=0
        while i<=pos:
            # the equal judge above should not be effective

            currentGas += gas[i]
            #print 'before' ,currentGas
            while currentGas < cost[i]:
                
                if pos < i :
                    return -1
                currentGas += (gas[pos]-cost[pos])
                pos = pos - 1
            #print 'after:' ,currentGas 
            
            currentGas = currentGas - cost[i]
            i+=1
        
        pos = (pos+1)%length
        return pos


    # n^2 time complexity
    def canCompleteCircuitFool(self,gas,cost):
        length = len(gas)
        if length <=1:
            return 0
        for i in xrange(0,length):
            currentGas  = gas[i]
            if currentGas < cost[i]:
                continue
            currentGas = currentGas-cost[i]
            end = -1
            for j in xrange(i+1,i+length-1):
                # normalize the index , remember it is a circuit!
                j = j % length
                end = j
                currentGas += gas[i]
                if currentGas < cost[i]:
                    break
            if end==i:
                return i

        return end


if __name__ == '__main__':
    ss = Solution()
    gas=[5]
    cost=[4]
    print ss.canCompleteCircuit(gas,cost)
