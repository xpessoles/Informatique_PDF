### Q1

def euler(F, a, b, y0, n):
    y = y0
    t = a
    les_t = [t]
    les_y = [y]
    h = (b - a) / n
    for k in range(n):
        t,y = t+h , y + h * F(t,y)
        les_t.append(t)
        les_y.append(y)
    return(les_t, les_y)


### Q2

import matplotlib.pyplot as plt
import numpy as np

def F(t,y):
    return(-t*y)

def f(t):
    return(np.exp(-t**2/2))


n = 100
les_t, les_y = euler(F, 0, 1, 1, n)
plt.plot(les_t, les_y)
plt.plot(les_t,[f(t) for t in les_t])
plt.show()


### Q3

# z=y' et z'=-1/y**2.

### Q4

# z(t+h)=z(t)-t/y(t)**2
# y(t+h)=y(t)+hz(t)

### Q5

#h=(b-a)/N
#les_t=[a+k*h for k in range(N+1)]

### Q6


def euler2(a,b,N,y0,yp0):
    h=(b-a)/N
    les_t=[a]
    les_y=[y0]
    les_z=[yp0]
    t,y,z=a,y0,yp0
    for k in range(N):
        t,y,z=t+h,y+h*z,z-h/y**2
        les_t.append(t)
        les_y.append(y)
        les_z.append(z)
    return(les_t,les_y,les_z)

### Q7

# y(t+h)=2*y(t)-y(t-h)-\Frac{h^2}{y(t)^2}

### Q8

# Pour le calcul du premier point, on aurait besoin de $y(a-h)$ qui n'est pas défini.

### Q9

# En négligeant le terme en O(h^3), y(a+h)=y(a)+y'(a).h+y''(a).h**2/2 ie y(a+h)=y0+h.yp0+y''(a).h**2/2.

### Q10

# Avec l'équation différentielle, on obtient y(a+h)=y0+h.yp0-h**2/2y_0^2.

### Q11


def verlet(a,b,N,y0,yp0):
    h=(b-a)/N
    t,ym,y,z = a+h,y0,y0+h*yp0-h**2/(2*y0**2),yp0-h/y0**2
    les_t=[a,t]
    les_y=[y0,y]
    les_z=[yp0,z]
    for k in range(1,N):
        t,ym,y,z=t+h,y,2*y-ym-h**2/y**2,z-h/y**2
        les_t.append(t)
        les_y.append(y)
        les_z.append(z)
    return(les_t,les_y,les_z)

### Q12

# Par dérivation, E'(t)=y'(t)y''(t)+y'(t)/y(t)**2=y'(t)*(y''(t)+1/y(t)**2=0 vu l'équation différentielle. Donc $E$ est une constante.

### Q13

a, b, N, y0, yp0 = 0, 1, 100, 1, 1

import matplotlib.pyplot as plt
Teuler,Yeuler,Zeuler=euler(a,b,N,y0,yp0)
Tverlet,Yverlet,Zverlet=verlet(a,b,N,y0,yp0)
Eeuler,Everlet=[],[]
for i in range(N+1):
    Eeuler.append(1/2*Zeuler[i]**2-1/Yeuler[i])
    Everlet.append(1/2*Zverlet[i]**2-1/Yverlet[i])
plt.plot(Teuler,Eeuler,label='euler')
plt.plot(Tverlet,Everlet,label='verlet')
plt.axis([a,b,-0.101,-0.099])
plt.legend()
plt.show()
