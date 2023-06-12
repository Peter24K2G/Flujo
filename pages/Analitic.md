# Solucion Analitica

## Solucion de Ecuacion de Flujo no Estacionario 

$$T \frac{\partial ^2h}{\partial x^2} = S \frac{\partial h}{\partial t}$$

$$\frac{1}{D_H}\frac{\partial ^2h}{\partial x^2} =\frac{\partial h}{\partial t} \quad D_H = \frac{S}{T}$$

Solucion a partir de Craig's

$$h = \sum_{n=2}^{\infty} \left(\frac{1}{L}\int_{{0}}^{{2L}} {h_i \sin \frac{n \pi x}{2L}} \: dx\right) \sin \frac{n \pi x}{2L}\exp\left(-\frac{n^2 \pi^2 t}{4L^2 D_H}\right)$$

Para el caso particular cuando $h_i$ es constante en todo el medio

$$h = \sum_{n=1}^{\infty} \frac{2h_i}{n \pi}(1-\cos n \pi)\left(\sin \frac{n \pi x}{2L}\right)\exp\left(-\frac{n^2 \pi t}{4L^2 D_H}\right)$$

Cuando $n$ es par $(1-\cos n\pi) = 0$, cuando $n$ es par $(1-\cos n\pi) = 2$ por lo tanto solamente los valores impares de $n$ son relevantes haciendo conveniente hacer la siguiente sustitucion

$$n = 2m + 1 \quad \& \quad M = \frac{\pi}{2}(2m+1)$$

Tambien es conveniente sustituir

$$T_v = \frac{t}{D_H L^2}$$

Obtenemos entonces la siguiente ecuacion:

$$
h = \sum_{m=0}^{\infty} \frac{2 h_i}{M} \left(\sin \frac{M x}{L}\right)\exp(-M T_v)
$$

---

## Solucion de Ecuacion de Consolidacion

$$\frac{k}{\gamma_w}\frac{\partial ^2u_e}{\partial z^2} = m_v \frac{\partial u_e}{\partial t}$$

$$c_v \frac{\partial ^2u_e}{\partial z^2} = \frac{\partial u_e}{\partial t} \quad c_v = \frac{k}{m_v \gamma_w}$$

Solucion propuesta por Craig's

$$u_e = \sum_{n=1}^{\infty} \left(\frac{1}{d}\int_{{0}}^{{2d}} {u_i \sin \frac{n \pi z}{2d}} \: dz\right)\left(\sin \frac{n \pi z}{2d}\right)\exp\left(-\frac{n^2 \pi^2 c_v t}{4d^2}\right)$$

Para el caso particular cuando $u_i$ es constante en todo el medio

$$u_e = \sum_{n=1}^{\infty} \frac{2u_i}{n\pi}(1-\cos n\pi ) \left(\sin \frac{n\pi z}{2d}\right)\exp\left(-\frac{n^2 \pi c_v t}{4d^2}\right)$$

Cuando $n$ es par $(1-\cos n\pi) = 0$, cuando $n$ es par $(1-\cos n\pi) = 2$ por lo tanto solamente los valores impares de $n$ son relevantes haciendo conveniente hacer la siguiente sustitucion

$$n = 2m + 1 \quad \& \quad M = \frac{\pi}{2}(2m+1)$$

Tambien es conveniente sustituir

$$T_v = \frac{c_v t}{d^2}$$

Obtenemos entonces la siguiente ecuacion:

$$
u_e = \sum_{n=0}^{\infty} \frac{2u_i}{M}\left(\sin \frac{M z}{d}\right)\exp(-M^2 T_v)
$$


---
## Codigo solucion (Python)
```python
import numpy as np
import matplotlib.pyplot as plt

 oo = 100 #Definimos el valor "infinito"
 delta = 1 #Definimos el valor del paso
 s = 1e-4 #Almacenamiento
 Tr = 0.00125 #Transmisividad [m^2/d]
 L = 30 #Longitud del medio [m]
 T = 30 #Cantidad de tiempo a evaluar
 hi = 10 #Cantidad inicial del nivel de agua [m]

DH = s / Tr  # Difusividad Hidráulica

m = np.arange(start=0, stop=oo, step=delta)  # Se crea el vector a iterar
t = np.arange(start=0.1, stop=oo, step=delta)  # Se crea el vector a iterar tiempo
x = np.arange(start=0, stop=L, step=delta)  # Se crea el vector a iterar distancia

M = (np.pi / 2) * (2 * m + 1)  # Se crea el término M a incluir en la ecuación
Tv = t / (DH * L ** 2)  # Se crea el término Tv a incluir en la ecuación

R = np.zeros((x.size, t.size))

for j in range(t.size):
    for i in range(x.size):
        h = np.zeros(m.size)
        for k in range(m.size):
            h[k] = (2 * hi / M[k]) * (np.sin(M[k] * x[i] / L)) * np.exp(-M[k] * Tv[j])
        R[i, j] = np.sum(h)

plt.plot(x, R[0:, :])
plt.xlabel('Distancia [m]')
plt.ylabel('Altura piezométrica [m]')
plt.title('Altura vs Distancia')
plt.grid(True)
plt.show()

```
