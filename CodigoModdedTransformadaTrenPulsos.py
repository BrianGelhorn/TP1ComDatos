# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:56:31 2024

@author: eneas
"""

import numpy as np
import matplotlib.pyplot as plt
import math
# Parámetros
frecuencia_repeticion = 3  # Frecuencia de repetición en Hz
amplitud = 1  # Amplitud del pulso
fs = 5000  # Frecuencia de muestreo

# Tiempo de simulación
t = np.arange(-10, 10, 1/fs)

# Duraciones de pulso a analizar
duraciones_pulsos = [0.02, 0.2, 0.5]  # Duraciones en segundos

# Crear una figura para visualizar los resultados
plt.figure(figsize=(12, 8))

for duracion_pulso in duraciones_pulsos:
    # Generación del tren de pulsos
    tren_pulsos = np.zeros_like(t)
    for i in range(int(t[0]*frecuencia_repeticion), math.ceil(t[-1] * frecuencia_repeticion)):
        tren_pulsos[int(i * fs / frecuencia_repeticion):int(i * fs / frecuencia_repeticion + duracion_pulso * fs)] = amplitud

    # Transformada de Fourier de la generatriz
    espectro = np.fft.fftshift(np.fft.fft(tren_pulsos, n=len(tren_pulsos)))/ len(tren_pulsos) #La dividimos por la cantidad de puntos que tiene el tren 
                                                                                              #de pulsos para que esté normalizada
    frecuencias = np.fft.fftshift(np.fft.fftfreq(len(espectro), d=1/fs))
    # espectro *= np.hamming(len(tren_pulsos))
    # Visualización del tren de pulsos
    plt.subplot(2, len(duraciones_pulsos), duraciones_pulsos.index(duracion_pulso) + 1)
    plt.plot(t, tren_pulsos)
    plt.title(f'Tren de Pulsos (Duración: {duracion_pulso}s)')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid()

    # Visualización del espectro
    plt.subplot(2, len(duraciones_pulsos), len(duraciones_pulsos) + duraciones_pulsos.index(duracion_pulso) + 1)
    plt.stem(frecuencias, abs(espectro)).markerline.set_visible(False)
    plt.title(f'Espectro de Frecuencia (Duración: {duracion_pulso}s)')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud')
    plt.grid()
    plt.xlim(-50, 50)  # Limitar el eje x para enfocarse en las frecuencias relevantes

plt.tight_layout()
plt.show()
