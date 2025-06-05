import numpy as np
import matplotlib.pyplot as plt

# Parámetros del tren de pulsos
f0 = 5      # Frecuencia de repetición (Hz)
tau = 0.1   # Duración de cada pulso (s)
A = 1       # Amplitud del pulso
N = 20      # Número de armónicos a representar

# Índices n
n = np.arange(-N, N + 1)

# Frecuencias en donde hay deltas
frecuencias = n * f0

# Amplitudes de los deltas (modulación sinc)
amplitudes = A * f0 * np.sinc(n * f0 * tau)

# Graficar el espectro
plt.figure(figsize=(8, 4))
plt.stem(frecuencias, amplitudes, basefmt=" ")
plt.title("Transformada de Fourier Analítica del Tren de Pulsos")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud (modulada por sinc)")
plt.grid(True)
plt.xlim(-60, 60)
plt.show()
