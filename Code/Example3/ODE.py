from sympy import *

#variable
t = symbols('t')
#dependent variable
y = symbols('y', cls=Function)

#Ordinary Differential Equation
deq = Eq( y(t).diff(t,2)+2*y(t).diff(t,1)+17*y(t), 0 )

result = dsolve( deq, ics= {y(0):2, y(t).diff(t).subs(t,0):2.6} )
print(result)

plot(result.rhs, xlim=(-10,0))
