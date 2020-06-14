from numpy import *
from scipy import *
from scipy import linalg
import string
import sys

p=0.5
s=0.0001
n=2
a=5.1
b=5

Z=rand(n,n)
ZT=Z.T
A=dot(ZT,Z)
e=n*0.000001
es=10e-16

n2=4
e2=n2*0.000001


def evalfa(x):
    f=x[0]**2+exp(x[0])+x[1]**4+x[1]**2-2*x[0]*x[1]+3
    return f

def evalga(x):
    g=array([2*x[0]+exp(x[0])-2*x[1],4*x[1]**3+2*x[1]-2*x[0]])
    return g

def evalha(x):
    H=array([[2+exp(x[0]),-2],[-2,12*x[1]**2+2]])
    return H


def evalFb(x):
    F=array([1.5-x[0]*(1-x[1]),
            2.25-x[0]*(1-x[1]**2),
            2.625-x[0]*(1-x[1]**3)])
    return F
def evalfb(x):
    F=evalFb(x)
    f=F[0]**2+F[1]**2+F[2]**2
    return f

def evalGb(x):
    F=evalFb(x)
    G=2*array([F[0]*array([-(1-x[1]),x[0]]),
               F[1]*array([-(1-x[1]**2),2*x[1]*x[0]]),
               F[2]*array([-(1-x[1]**3),3*x[1]**2*x[0]])])
    return G

def evalgb(x):
    G=evalGb(x)
    g=G[0]+G[1]+G[2]
    return g

def evalhb(x):
    F=evalFb(x)
    H=2*(F[0]*array([[0,1],[1,0]])+array([[(1-x[1])**2,-x[0]*(1-x[1])],[-x[0]*(1-x[1]),x[0]**2]])+
         F[1]*array([[0,2*x[1]],[2*x[1],2*x[0]]])+array([[(1-x[1]**2)**2,-(1-x[1]**2)*2*x[1]*x[0]],[-(1-x[1]**2)*2*x[1]*x[0],4*x[1]**2*x[0]**2]])+
         F[2]*array([[0,3*x[1]**2],[3*x[1]**2,6*x[1]*x[0]]])+array([[(1-x[1]**3)**2,-(1-x[1]**3)*3*x[1]**2*x[0]],[-(1-x[1]**3)*3*x[1]**2*x[0],9*x[1]**4*x[0]**2]]))
    return H

def evalfc(x):
    f=0.5*dot(x.T,dot(A,x))
    return f

def evalgc(x):
    g=dot(A,x)
    return g

def evalhc(x):
    H=A
    return H

def evalfd(x):
    f=(x[1]-(5.1*x[0]**2)/(4*pi**2)+(5*x[0])/pi-6)**2+10*(1-(1/8*pi))*cos(x[0])+10
    return f

def evalgd(x):
    g=array([(a**2*x[0]**3)/(4*pi**4)-(3*a*b*x[0]**2)/(2*pi**3)+(6*a*x[0]+2*b**2*x[0]-a*x[0]*x[1])/pi**2+(2*b*x[1]-12*b)/pi-10*(1-1/8*pi)*sin(x[0]),2*x[1]-(a*x[0]**2)/(2*pi**2)+(2*b*x[0])/pi-12])
    return g

def evalF1e(x):
    i=0
    f1=0
    while i<n2:
        f1=f1+x[i]**2
        i=i+1
    f1=-0.2*((1.0/n2)*f1)**(1.0/2)
    return f1

def evalF2e(x):
    i=0
    f2=0
    while i<n2:
        f2=f2+cos(2*pi*x[i])
        i=i+1
    f2=f2*(1.0/n2)    
    return f2

def evalfe(x):
    f1=evalF1e(x)
    f2=evalF2e(x)
    f=-20*exp(f1)-exp(f2)+20+exp(1)
    return f

def evalG1e(x):
    f1=evalF1e(x)
    g1=array(0.04*x/(n2*f1))
    return g1

def evalG2e(x):
    g2=array(((-2*pi)/n2)*sin(2*pi*x))
    return g2

def evalge(x):
    f1=evalF1e(x)
    f2=evalF2e(x)
    g1=evalG1e(x)
    g2=evalG2e(x)
    g=-20*exp(f1)*g1-exp(f2)*g2
    return g


def main():
    args=sys.argv[1:]
    problem=string.atoi(args[0])
    method=string.atoi(args[1])
    step=string.atoi(args[2])
    
    if problem == 1:
        if method == 1:
            if step == 1:
                x=array([0.3,5])
                g=evalga(x)
                k=1
                while linalg.norm(g)>e:
                    g=evalga(x)
                    d=-g
                    t=1
                    l=linalg.norm(g)
                    f=evalfa(x)
                    while evalfa(x+t*d)>f+s*t*(-(l**2)):
                        t=t*p
                    x=x+t*d
                    k=k+1
                print 'k=',k-1    
                print 'x=',x

            elif step == 2:
                x=array([0.3,5])
                g=evalga(x)
                k=1
                while linalg.norm(g)>e:
                    g=evalga(x)
                    d=-g
                    t=1
                    l=linalg.norm(g)
                    f=evalfa(x)
                    i=inner(d,g)
                    while evalfa(x+t*d)>f+(s*t*i):
                        if -(i*(t**2))/(2*(evalfa(x+t*d)-f-i*t))<0.1*t or -(i*(t**2))/(2*(evalfa(x+t*d)-f-i*t))>0.9*t:
                            t=0.5*t
                        else:
                            t=-(i*(t**2))/(2*(evalfa(x+t*d)-f-i*t))
                    x=x+t*d
                    k=k+1
                print 'k=',k-1
                print 'x=',x

        elif method == 2:
            if step == 2:
                x=array([1.0,5.0])
                g=evalga(x)
                k=1
                while linalg.norm(g)>e:
                    g=evalga(x)
                    f=evalfa(x)
                    H=evalha(x)
                    L=linalg.cho_factor(H)
                    d=linalg.cho_solve(L,-g)
                    t=1
                    i=inner(d,g)
                    while evalfa(x+t*d)>f+(s*t*i):
                        if -(i*(t**2))/(2*(evalfa(x+t*d)-f-i*t))<0.1*t or -(i*(t**2))/(2*(evalfa(x+t*d)-f-i*t))>0.9*t:
                            t=0.5*t
                        else:
                            t=-(i*(t**2))/(2*(evalfa(x+t*d)-f-i*t))
                    x=x+t*d
                    k=k+1
                print 'k=',k-1
                print 'x=',x

            elif step == 1:
                x=array([1.0,5.0])
                g=evalga(x)
                k=1
                while linalg.norm(g)>e:
                    g=evalga(x)
                    f=evalfa(x)
                    H=evalha(x)
                    L=linalg.cho_factor(H)
                    d=linalg.cho_solve(L,-g)
                    t=1
                    i=inner(d,g)
                    while evalfa(x+t*d)>f+s*t*i:
                        t=t*p
                    x=x+t*d
                    k=k+1
                print 'k=',k-1    
                print 'x=',x

    elif problem == 2:
        if method == 1:
            if step == 1:
                x=array([1.0,1.0])
                g=evalgb(x)
                k=1
                while linalg.norm(g)>e:
                    g=evalgb(x)
                    f=evalfb(x)
                    d=-g
                    t=1
                    while evalfb(x+t*d)>f+s*t*(-(linalg.norm(g)**2)):
                        t=t*p
                    x=x+t*d
                    k=k+1
                print 'k=',k-1
                print 'x=',x

            elif step == 2:
                x=array([1.0,1.0])
                g=evalgb(x)
                k=1
                while linalg.norm(g)>e:
                    g=evalgb(x)
                    f=evalfb(x)
                    d=-g
                    t=1
                    i=inner(d,g)
                    while evalfb(x+t*d)>f+(s*t*i):
                        if -(i*(t**2))/(2*(evalfb(x+t*d)-f-i*t))<0.1*t or -(i*(t**2))/(2*(evalfb(x+t*d)-f-i*t))>0.9*t:
                            t=0.5*t
                        else:
                            t=-(i*(t**2))/(2*(evalfb(x+t*d)-f-i*t))
                    x=x+t*d
                    k=k+1
                print 'k=',k-1
                print 'x=',x

        elif method == 2:
            if step == 1:
                x=array([1.0,1.0])
                g=evalgb(x)
                k=1
                while linalg.norm(g)>e:
                    g=evalgb(x)
                    f=evalfb(x)
                    H=evalhb(x)
                    T=1
                    B=H
                    
                    while True:
                        try:
                            L=linalg.cho_factor(B)
                            d=linalg.cho_solve(L,-g)
                            t=1
                            i=inner(d,g)
                            while evalfb(x+t*d)>f+s*t*i:
                                t=t*p
                            break
                        except linalg.LinAlgError:
                            T=T*2
                            B=H+T*array([[1,0],[0,1]])
                    x=x+t*d
                    k=k+1
                print 'k=',k-1
                print 'x=',x

            elif step == 2:
                x=array([1.0,1.0])
                g=evalgb(x)
                k=1
                while linalg.norm(g)>e:
                    g=evalgb(x)
                    f=evalfb(x)
                    H=evalhb(x)
                    T=1
                    B=H
                    while True:
                        try:
                            L=linalg.cho_factor(B)
                            d=linalg.cho_solve(L,-g)
                            break
                        except linalg.LinAlgError:
                            T=T*2
                            B=H+T*array([[1,0],[0,1]])

                    t=1
                    i=inner(d,g)
                    while evalfb(x+t*d)>f+(s*t*i):
                        if -(i*(t**2))/(2*(evalfb(x+t*d)-f-i*t))<0.1*t or -(i*(t**2))/(2*(evalfb(x+t*d)-f-i*t))>0.9*t:
                            t=0.5*t
                        else:
                            t=-(i*(t**2))/(2*(evalfb(x+t*d)-f-i*t))
                    x=x+t*d
                    k=k+1
                print 'k=',k-1
                print 'x=',x
                
    elif problem == 3:
        if method == 1:
            if step == 1:
                x=ones(n)
                g=evalgc(x)
                k=1
                while linalg.norm(g)>e:
                    g=evalgc(x)
                    d=-g
                    t=1
                    l=linalg.norm(g)
                    f=evalfc(x)
                    while evalfc(x+t*d)>f+s*t*(-(l**2)):
                        t=t*p1
                    x=x+t*d
                    k=k+1
                print 'k=',k-1
                print 'x=',x

            elif step == 2:
                 x=ones(n)
                 g=evalgc(x)
                 k=1
                 while linalg.norm(g)>e:
                     g=evalgc(x)
                     d=-g
                     t=1
                     l=linalg.norm(g)
                     f=evalfc(x)
                     i=inner(d,g)
                     while evalfc(x+t*d)>f+(s*t*i):
                         if -(i*(t**2))/(2*(evalfc(x+t*d)-f-i*t))<0.1*t or -(i*(t**2))/(2*(evalfc(x+t*d)-f-i*t))>0.9*t:
                             t=0.5*t
                         else:
                             t=-(i*(t**2))/(2*(evalfc(x+t*d)-f-i*t))
                     x=x+t*d
                     k=k+1
                 print 'k=',k-1
                 print 'x=',x

               
        elif method == 2:
            if step == 1: 
                 x=ones(n)
                 g=evalgc(x)
                 k=1
                 while linalg.norm(g)>e:
                     g=evalgc(x)
                     f=evalfc(x)
                     H=evalhc(x)
                     L=linalg.cho_factor(H)
                     d=linalg.cho_solve(L,-g)
                     t=1
                     i=inner(d,g)
                     while evalfc(x+t*d)>f+s*t*i:
                         t=t*p   
                     x=x+t*d
                     k=k+1
                 print 'k=',k-1
                 print 'x=',x

            elif step == 2:
                 x=ones(n)
                 g=evalgc(x)
                 k=1
                 while linalg.norm(g)>e:
                     g=evalgc(x)
                     f=evalfc(x)
                     H=evalhc(x)
                     L=linalg.cho_factor(H)
                     d=linalg.cho_solve(L,-g)
                     t=1
                     i=inner(d,g)
                     while evalfc(x+t*d)>f+(s*t*i):
                         if -(i*(t**2))/(2*(evalfc(x+t*d)-f-i*t))<0.1*t or -(i*(t**2))/(2*(evalfc(x+t*d)-f-i*t))>0.9*t:
                             t=0.5*t
                         else:
                             t=-(i*(t**2))/(2*(evalf(x+t*d)-f-i*t))       
                     x=x+t*d
                     k=k+1
                 print 'k=',k-1
                 print 'x=',x

    elif problem == 4:
        if method == 3:
            if step == 2:
                 x=array([0,0])
                 d=1
                 k=1
                 while linalg.norm(d)>e:
                     print 'd=',d
                     g=evalgd(x)
                     d=array([max(-5,min(x[0]-g[0],10)),max(0,min(x[1]-g[1],15))])-x
                     f=evalfd(x)
                     t=1
                     i=inner(d,g)
                     while evalfd(x+t*d)>f+(s*t*i):
                         if -(i*(t**2))/(2*(evalfd(x+t*d)-f-i*t))<0.1*t or -(i*(t**2))/(2*(evalfd(x+t*d)-f-i*t))>0.9*t:
                             t=0.5*t
                         else:
                             t=-(i*(t**2))/(2*(evalfd(x+t*d)-f-i*t))
                     x=x+t*d
                     k=k+1
                 print 'k=',k
                 print 'x=',x

            elif step == 1:
                x=array([0,0])
                d=1
                k=1
                while linalg.norm(d)>e:
                    g=evalgd(x)
                    d=array([max(-5,min(x[0]-g[0],10)),max(0,min(x[1]-g[1],15))])-x
                    f=evalfd(x)
                    t=1
                    while evalfd(x+t*d)>f+s*t*(-(linalg.norm(g)**2)):
                        t=t*p
                    x=x+t*d
                    k=k+1
                print 'k=',k
                print 'x=',x

    elif problem == 5:
        if method == 3:
            if step == 1:
                x=array([2,1,-2,-1])
                d=1
                k=1
                while linalg.norm(d)>e2:
                    g=evalge(x)
                    d=maximum(-32.768,minimum(x-g,32.768))-x
                    f=evalfe(x)
                    t=1
                    while evalfe(x+t*d)>f+s*t*(inner(d,g)):
                        t=t*p   
                    x=x+t*d
                    if t*linalg.norm(d,inf)<=es*max(1,linalg.norm(x,inf)):
                        break
                    k=k+1
                print 'k=',k
                print 'x=',x

            elif step == 2:
                x=array([2,1,-2,-1])
                d=1
                k=1
                while linalg.norm(d)>e2:
                    g=evalge(x)
                    d=maximum(-32.768,minimum(x-g,32.768))-x
                    f=evalfe(x)
                    t=1
                    i=inner(d,g)
                    while evalfe(x+t*d)>f+(s*t*i):
                        if -(i*(t**2))/(2*(evalfe(x+t*d)-f-i*t))<0.1*t or -(i*(t**2))/(2*(evalfe(x+t*d)-f-i*t))>0.9*t:
                            t=0.5*t
                        else:
                            t=-(i*(t**2))/(2*(evalfe(x+t*d)-f-i*t))
                    x=x+t*d
                    if t*linalg.norm(d,inf)<=es*max(1,linalg.norm(x,inf)):
                        break
                    k=k+1
                print 'k=',k
                print 'x=',x
   
main()
