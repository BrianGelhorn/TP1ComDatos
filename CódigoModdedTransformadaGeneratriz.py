# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:56:31 2024

@author: eneas
"""

import numpy as np
import matplotlib.pyplot as plt
import math
# Parámetros
frecuencia_repeticion = 1  # Frecuencia de repetición en Hz
amplitud = 1  # Amplitud del pulso
fs = 1000  # Frecuencia de muestreo

# Tiempo de simulación
t = np.arange(-0.5, 0.5, 1/fs)

# Duraciones de pulso a analizar
duraciones_pulsos = [0.02, 0.2, 0.5]
# Crear una figura para visualizar los resultados
plt.figure(figsize=(12, 8))
for duracion_pulso in duraciones_pulsos:
    # Generación del tren de pulsos
    generatriz = np.zeros_like(t)
    for i in range(math.ceil(t[-1] * frecuencia_repeticion)):
        generatriz[int(len(generatriz)//2-(duracion_pulso/2)*fs):int(len(generatriz)//2+(duracion_pulso/2)*fs)] = amplitud
        #Creo un pulso siendo este la generatriz centrada en 0

    # Transformada de Fourier de la generatriz
    espectro = np.fft.fftshift(np.fft.fft(generatriz, n=len(generatriz)))/ len(generatriz)
    frecuencias = np.fft.fftshift(np.fft.fftfreq(len(espectro), d=1/fs))
    espectroContinuo = amplitud*duracion_pulso*np.sinc(frecuencias*duracion_pulso)

    # Visualización del tren de pulsos
    plt.subplot(2, len(duraciones_pulsos), duraciones_pulsos.index(duracion_pulso) + 1)
    plt.plot(t, generatriz)
    plt.title(f'Tren de Pulsos (Duración: {duracion_pulso}s)')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid()

    # Visualización del espectro
    plt.subplot(2, len(duraciones_pulsos), len(duraciones_pulsos) + duraciones_pulsos.index(duracion_pulso) + 1)
    plt.stem(frecuencias, abs(espectro))
    plt.plot(frecuencias, abs(espectroContinuo))
    plt.title(f'Espectro de Frecuencia (Duración: {duracion_pulso}s)')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud')
    plt.grid()
    plt.xlim(-50, 50)  # Limitar el eje x para enfocarse en las frecuencias relevantes

plt.tight_layout()
plt.show()
