v = [1,2,3,4]

# Overwrite the function moving_avg
def moving_avg():
    avgSum = 0
    term = 0
    numTerms = [1, 1]
    while True:
        ##First 4 lines displays what happens in the code
        #print ('avgSum', avgSum)
        #print ('term', term)
        #print ('Number of terms', numTerms[0])
        #print ()
        
        term = yield avgSum/numTerms[0] ##Set the current term and return the updated moving average
        avgSum += term
        numTerms.pop(0) ##Removes the element indicating the current number of terms
        numTerms.append(numTerms[-1] + 1) ##Adds one higher number to the end of the list

# Testing your function
ma = moving_avg()
next(ma)

mavg = []
for value in v:
    mavg.append(ma.send(value))
    
print (mavg) # Should print: [1.0, 1.5, 2.0, 2.5]