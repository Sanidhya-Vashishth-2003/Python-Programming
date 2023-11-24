import time as t
for i in range(10):
    t.sleep(.2)
    print(" "*(10-i)+"* "*(i+1))
for i in range(10,-1,-1):
    t.sleep(.2)
    print(" "*(10-i)+"* "*(i+1))
