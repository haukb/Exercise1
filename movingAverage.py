v = [1,2,3,4]

# Overwrite the function moving_avg
def moving_avg():
    total = 0.0
    counter = 0
    avg = None
    
    while True:
        term = yield avg 
        total += term
        counter += 1
        avg = total/counter

# Testing your function
ma = moving_avg()
next(ma)

mavg = []
for value in v:
    mavg.append(ma.send(value))
    
print (mavg) # Should print: [1.0, 1.5, 2.0, 2.5]