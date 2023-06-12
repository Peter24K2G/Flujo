# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 16:36:44 2023

@author: Peter
"""

import numpy as np
import matplotlib.pyplot as plt

"""
Definimos las cantidades de los valores que se van a evaular en las diferente variables
oo = infinito ----> 1000     &       δ = delta ----> 1
L = 30m, ΔL = L/δ
t = 365d, Δt = L/δ
Ss = Almacenamiento específico ----> 0.0001ft^(-1)
K  = Conductividad hidráulica  ----> 3.8e-2 m/d
"""
# oo = 100 #Definimos el valor "infinito"
# delta = 1 #Definimos el valor del paso
# s = 1e-4 #Almacenamiento
# Tr = 0.00125 #Transmisividad [m^2/d]
# L = 30 #Longitud del medio [m]
# T = 30 #Cantidad de tiempo a evaluar
# hi = 10 #Cantidad inicial del nivel de agua [m]

def analitic(oo=100,s=1e-4,Tr=0.00125,L=30,T=30,hi=10,dt=1):
    delta =1
    DH = s/Tr #Difusividad Hidráulica
    
    m = np.arange(start = 0, stop = oo, step = delta) #Se crea el vector a iterar
    t = np.arange(start = 0,stop = T,step = delta)#Se crea el vector a iterar tiempo
    x = np.arange(start = 0, stop = L, step = delta) #Se crea el vector a iterar distancia
    
    M = (np.pi/2)*(2*m + 1) #Se crea el término M a incluir en la ecuación
    Tv = t/(DH*L**2) #Se crea el término Tv a incluir en la ecuación
    
    R = np.zeros((x.size,t.size))
    
    for j in range(t.size):
        for i in x:
            h = np.zeros(m.size)
            for k in m:
                h[k] = (2*hi/M[k])*(np.sin(M[k]*x[i]/L))*np.exp(-M[k]*Tv[j])
            R[i,j] = np.sum(h)
            
    fig, ax = plt.subplots(1,1) 
    ax.plot(x,R[0:,np.arange(0,R.shape[1],dt)])
    ax.set_title("Cambio del nivel del agua")
    ax.set_xlabel("Longitud del medio [m]")
    ax.set_ylabel("Altura [m]")
    ax.grid(True)
    Parameters = "Almacenamiento: " + str(s/100) +"\n Transmisividad [m2/d]: "+str(Tr)
    ax.text(1.3*L,hi/2,Parameters,fontsize=12,ha='center')
    return fig
    
def numeric(n=9, m=1014, Tr=0.00125, s=1e-4, X=30, Hi=10, Dt=1):
    
    # Espaciamiento en dirección x
    dx = X / (n - 1)  # Intervalo de longitud [1/m]
    dt =  (s * dx**2) / (2 * Tr)  # Intervalo de tiempo [d]
    A = (dt * Tr) / (dx**2 * s)
    # T = m * dt
    
    Hb = np.zeros((n, m))
    
    # Definición de bordes de contorno
    for i in range(n):
        # x = i * dx
        Hb[i, 0] = Hi
    
    for i in range(m - 1):
        for j in range(n - 2):
            Hb[0, i + 1] = 0
            Hb[n - 1, i + 1] = 2 * A * Hb[n - 2, i] + (1 - 2 * A) * Hb[n - 1, i]
            Hb[j + 1, i + 1] = A * Hb[j + 2, i] + (1 - 2 * A) * Hb[j + 1, i] + A * Hb[j, i]
    
    dist = np.zeros((n, 1))
    dist[0, 0] = 0
    for i in range(n - 1):
        dist[i + 1, 0] = (i + 1) * dx
        
    # Se almacena los tiempos que corresponden a cada serie
    # para luego poner el label de manera automática
    time = [str((i - 1) * dt) for i in range(1, m + 1)]
    
    # Plot
    fig , ax = plt.subplots(1,1)
    ax.plot(dist, Hb[:,np.arange(0,Hb.shape[1],Dt)])
    ax.set_title("Cambio del nivel del agua")
    ax.set_xlabel("Longitud del medio [m]")
    ax.set_ylabel("Altura [m]")
    ax.grid(True)
    Parameters = "Almacenamiento: " + str(s/100) +"\n Transmisividad [m2/d]: "+str(Tr)
    ax.text(1.35*X,Hi/2,Parameters,fontsize=12,ha='center')
    return fig
    
        
    
        
    
    
    
        