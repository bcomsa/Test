# ex51b.py
from __future__ import print_function

def count(func):
    print(' func = ',func)
    func.counter = 0
    def decorator(*args):
        func.counter += 1
        print(' counter of {} = {}'.
              format(func.__name__,func.counter))
        print('\t args =',args)
        ret = func(*args)
        print('\t Result =',ret)
        return ret
    return decorator

def calc1(a,b,c):
    return 2*a+3*b+4*c

def calc2(a,b,c):
    return 3*a+4*b+5*c

def calc3(a,b,c):
    return 4*a+5*b+6*c

def calc4(a,b):
    return 9*a+10*b

# Function decorations
calc1 = count(calc1)
calc2 = count(calc2)
calc3 = count(calc3)
calc4 = count(calc4)

a=calc1(1,2,3)
calc2(1,2,3)
calc3(1,2,3)
calc1(2,3,4)
calc2(2,3,4)
calc3(2,3,4)
calc4(1,2)
calc4(2,3)
for i in range(2):
    calc4(i,i+1)
print(' Value of a is ',a)