"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from sympy import*
from sympy.plotting import*
import numpy as np

def grad(f,v):
    n = len(v)
    g = []
    for i in range(n):
        d = diff(f,v[i])
        g += [d]
    return(g)

def ev_grad(g,v,u):
    n = len(v)
    c = []
    for i in range(n):
        t = g[i]
        for j in range(n):
            t = t.subs(v[j],u[i])
        c += [float(t)]
    return(c)

def ev_sol(f,v,u):
    fm = f.subs(v[0],u[0])
    for i in range(1,len(v)):
        fm = fm.subs(v[i],u[i])
    return(fm)

def cal_paso(f,g,v,u):
    c = ev_grad(g,v,u)
    t = Symbol('t')
    xt = []
    for i in range(len(v)):
        xt += [float(u[i]) - t*float(c[i])]
    fs = f.subs(v[0],u[0])
    for i in range(1,len(v)):
        fs = fs.subs(v[i],xt[i])
    df = diff(fs,t)
    ddf = diff(df,t)
    s = 1
    for i in range(5):
        s = s - float(df.subs(t,s))/float(ddf.subs(t,s))
    return(s)

def metodo_grad(f,v,u,e,it):
    g = grad(f,v)
    print('  0 {:8.5f} {:8.5f} {:8.5f}'.format(u[0],u[1],u[2]))
    for k in range(it): 
        c = ev_grad(g,v,u)
        fm = ev_sol(f,v,u)
        s = cal_paso(f,g,v,u)
        uk = []
        for i in range(len(c)):
            uk += [float(u[i]) - s*float(c[i])]
        u = uk.copy()
        print('{:3d} {:8.5f} {:8.5f} {:8.5f} {:12.5e} {:8.5f}'.format(k+1,u[0],u[1],u[2],float(fm),s))

x,y,z = symbols('x y z')

Z = (3*x-cos(y*z)-(1/2))**2 + ((x**2)-625*(y**2))**2 + (exp(-x*y) + 20*z + (10*pi - 3)/3)**2

v = [x,y,z]
u = [0,0,0]

metodo_grad(Z,v,u,1e-10,40)