# Método de Diferencias Finitas para Resolver Ecuaciones Diferenciales Parabólicas

El método de diferencias finitas es una técnica numérica utilizada para aproximar soluciones a ecuaciones diferenciales. Es particularmente útil para resolver ecuaciones diferenciales parabólicas parciales (EDP), las cuales involucran una variable dependiente del tiempo y una o más variables espaciales. En este método, el dominio continuo se discretiza en una rejilla de puntos y las derivadas en la ecuación diferencial se aproximan utilizando aproximaciones de diferencias finitas.

## Enunciado del Problema

Consideremos una EDP parabólica general de la forma:

$$\frac{du}{dt} = D\frac{d^2u}{dx^2}$$


donde $u$ representa la función desconocida, $t$ es el tiempo, $x$ es la variable espacial y $D$ es una constante que representa el coeficiente de difusión.

## Discretización

Para aplicar el método de diferencias finitas, primero discretizamos el dominio continuo en una rejilla de puntos. Elegimos un paso de tiempo $\Delta t$ y un paso espacial $\Delta x$, y dividimos el dominio en consecuencia. Sea $u(i, j)$ la aproximación numérica de $u$ en el $i-ésimo$ punto espacial y el $j-ésimo$ paso de tiempo.

Utilizando la aproximación de diferencias centrales para la segunda derivada, podemos expresar la ecuación diferencial en términos de los puntos de la rejilla:

$$(u(i, j+1) - u(i, j))/\Delta t = D\cdot (u(i-1, j) - 2u(i, j) + u(i+1, j))/(\Delta x)^2$$


## Esquema de Avance en el Tiempo

Para resolver la parte dependiente del tiempo de la ecuación, utilizamos un esquema de avance en el tiempo como el método de Euler hacia adelante o el método de Euler hacia atrás. En este ejemplo, utilizaremos el método de Euler hacia adelante.

Utilizando el método de Euler hacia adelante, podemos reescribir la ecuación como:

$$u(i, j+1) = u(i, j) + (D \cdot \Delta t/(\Delta x)^2) \cdot (u(i-1, j) - 2u(i, j) + u(i+1, j))$$


## Condiciones de Contorno

Para definir completamente el problema, debemos especificar las condiciones de contorno. Estas condiciones determinan los valores de `u` en los puntos límite del dominio.

Por ejemplo, si tenemos condiciones de contorno de Dirichlet donde `u` está especificado en los límites, podemos establecer `u(0, j)` y `u(n, j)` (donde `n` es el número de puntos espaciales) a sus respectivos valores límite en cada paso de tiempo.

## Solución Iterativa

Para obtener la solución numérica, comenzamos con una condición inicial `u(i, 0)` en `t = 0` y utilizamos el esquema de avance en el tiempo para calcular de manera iterativa `u(i, j+1)` en cada paso de tiempo. Repetimos este proceso hasta que alcancemos el tiempo final deseado.

## Ventajas y Limitaciones

El método de diferencias finitas es ampliamente utilizado debido a su simplicidad y flexibilidad. Permite resolver una amplia variedad de ecuaciones diferenciales parabólicas y puede manejar dominios espaciales y temporales complicados.

Sin embargo, el método de diferencias finitas también tiene algunas limitaciones. La precisión de la solución depende de la elección de los pasos de tiempo y espaciales, y se requiere una malla lo suficientemente fina para obtener resultados precisos. Además, el método puede volverse computacionalmente costoso para problemas con dominios grandes o geometrías complicadas.

## Conclusiones

En resumen, el método de diferencias finitas es una técnica numérica poderosa para resolver ecuaciones diferenciales parabólicas. A través de la discretización del dominio y la aproximación de las derivadas, podemos obtener soluciones aproximadas a estas ecuaciones. Aunque el método tiene sus limitaciones, sigue siendo una herramienta valiosa en la modelización y resolución de problemas en diversos campos científicos y de ingeniería.

```python
import numpy as np
import matplotlib.pyplot as plt

n = 9
m = 1014
Tr = 0.00125
s = 1e-4
X = 30
Hi = 10
Dt = 1

# Espaciamiento en dirección x
dx = X / (n - 1)  # Intervalo de longitud [1/m]
dt = (s * dx**2) / (2 * Tr)  # Intervalo de tiempo [d]
A = (dt * Tr) / (dx**2 * s)

Hb = np.zeros((n, m))

# Definición de bordes de contorno
for i in range(n):
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

time = [str((i - 1) * dt) for i in range(1, m + 1)]

fig, ax = plt.subplots(1, 1)
ax.plot(dist, Hb[:, np.arange(0, Hb.shape[1], Dt)])
ax.set_title("Cambio del nivel del agua")
ax.set_xlabel("Longitud del medio [m]")
ax.set_ylabel("Altura [m]")
ax.grid(True)
parameters = "Almacenamiento: " + str(s / 100) + "\n Transmisividad [m2/d]: " + str(Tr)
ax.text(1.35 * X, Hi / 2, parameters, fontsize=12, ha='center')

plt.show()

```
