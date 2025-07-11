from numpy import sqrt
from sympy.plotting import *
from sympy import Symbol
#ax^2 +bx +c

def zeros(a,b,c):
    D=sqrt(b*b-4*a*c)
    x1=(-b +D)/(2*a)
    x2=(-b-D)/(2*a)
    print("First second root",x1,x2)
    
def printGraph(a,b,c):
    x = Symbol('x')
    y = a*x**2 + b*x + c
    plot(y, (x, -10, 10), title='Quadratic Function', xlabel='x', ylabel='f(x)')
    

if __name__ == "__main__":1
    print("Quadratic equati2on solver")
    a=input("Enter a:  ")
    b=input("Enter b:  ")
    c=input("Enter c:  ")
    zeros(float(a),float(b),float(c))
    printGraph(float(a),float(b),float(c))
    
