import numpy as np
import matplotlib.pyplot as plt
import math


frequency = 3  # Measured in Hz
amplitude = 1  # Amplitude of the pulse
fs = 5000  # Frequency of samples

# Time of simulation
t = np.arange(-0.5, .5, 1/fs)

# Duration of the pulses to analyze
pulses_duration = [0.02, 0.2, 0.5]  # Measured in Seconds

plt.figure(figsize=(12, 8))
for pulse_duration in pulses_duration:
    # Generation of pulse train
    generatriz = np.zeros_like(t)
    for i in range(math.ceil(t[-1] * frequency)):
        generatriz[int(len(generatriz)//2-(pulse_duration/2)*fs):int(len(generatriz)//2+(pulse_duration/2)*fs)] = amplitude
        #I give the value of the amplitud from the index i plus/less the duration of the pulse divided 2 to both sides so I have it centered at 0

    # Fourier transform of the pulse. (Non Periodic Signal)
    spectrum = np.fft.fftshift(np.fft.fft(generatriz, n=len(generatriz)))/ len(generatriz) #I divide it for the amount of points that the pulse train has to 
                                                                                           #normalize the FFT and we apply shift to map also the negative values
    frequencies = np.fft.fftshift(np.fft.fftfreq(len(spectrum), d=1/fs))
    continuousSpectrum = amplitude*pulse_duration*np.sinc(frequencies*pulse_duration) 
    #The formula calculated in an analitical way to show the wave representing the Fourier Transform

    # Visualization of each Pulse Train
    plt.subplot(2, len(pulses_duration), pulses_duration.index(pulse_duration) + 1)
    plt.plot(t, generatriz)
    plt.title(f'Generatriz Pulse (Duration: {pulse_duration}s)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()

    # Visualization of each Spectrum
    plt.subplot(2, len(pulses_duration), len(pulses_duration) + pulses_duration.index(pulse_duration) + 1)
    plt.stem(frequencies, abs(spectrum)).markerline.set_visible(False)
    plt.plot(frequencies, abs(continuousSpectrum), "r")
    plt.title(f'Frecuency Spectrum (Duration: {pulse_duration}s)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid()
    plt.xlim(-30, 30) #I limit the axis to focus on the most relevant frequencies


plt.tight_layout()
plt.show()
