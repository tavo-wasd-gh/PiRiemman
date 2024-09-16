#!/usr/bin/env python

# Término de la serie de Leibniz para aproximar pi
def leibniz_pi_integral(punto_actual):
    return 4/(1 + punto_actual**2)

# Sumatoria de Riemman tomando un rango, interaciones y función
def riemman_sum(pinicial, pfinal, iteraciones, funcion):
    # Salto en x por cada iteración
    base = (pfinal - pinicial) / iteraciones
    # Definición del primer valor de x es:
    # Distancia entre el punto inicial y el salto
    xpos = pinicial + base/2

    # La sumatoria inicia en 0
    suma = 0.0
    for _ in range(iteraciones):
        # Sumar el valor del área al total
        suma += funcion(xpos) * base
        # Delta x para la siguiente evaluación
        xpos += base

    # Retorna la suma final
    return suma

print(riemman_sum(0, 1, 1000, leibniz_pi_integral))
