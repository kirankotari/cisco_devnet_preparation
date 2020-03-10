# Understanding python passing args

## Q1
m = [1, 2, 3]

def new_list(f):
    f.append(4)
    return f

n = new_list(m)
## what does n and m have? 

## Q2
m = [1, 2, 3]

def replace(f):
    f = [4, 5, 6]
    return f

n = replace(m)
## what does n and m have? 

## Q3
m = [1, 2, 3]

def new_list1(f):
    f[0] = 4
    f[1] = 5
    f[2] = 6
    return f

n = new_list(m)
## what does n and m have? 

## Q4
m = [1, 2, 3]
def f(d):
    return d

n = f(m)
## id() of n and m are same or different?

# Understanding python scope
## Q5
from math import e
def myE():
    global e
    print(e)
    e = -1234

myE() 
## what does this function prints?
myE() 
## what does this function prints?
print(e) 
## whats the value in e? 

## Q6
x = 10
y = 20

def outer():
    z = 30
    def inner():
        x = 40
        print(f'x is {x}')
        print(f'y is {y}')
        print(f'z is {z}')
        print(len('abc'))
    inner()
outer()

## chose scope of each variable printing from the below
## Global or Local or Built-in or Enclosing 

## Q7

