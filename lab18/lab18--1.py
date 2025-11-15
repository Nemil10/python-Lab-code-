import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fs1, x = wavfile.read("audio.wav")
fs2, h = wavfile.read("impulse.wav")

# Convert to float
x = x.astype(np.float32)
h = h.astype(np.float32)

linear_conv = np.convolve(x, h)
print("Linear Convolution:", linear_conv)

# Determine length
N = max(len(x), len(h))

# Zero padding
x_pad = np.pad(x, (0, N - len(x)), mode='constant')
h_pad = np.pad(h, (0, N - len(h)), mode='constant')

X_fft = np.fft.fft(x_pad)
H_fft = np.fft.fft(h_pad)

circular_conv = np.fft.ifft(X_fft * H_fft)
circular_conv = np.real(circular_conv)

print("Circular Convolution:", circular_conv)

plt.figure(figsize=(10,6))
plt.plot(linear_conv, label="Linear Convolution")
plt.plot(circular_conv, label="Circular Convolution")
plt.title("Linear vs Circular Convolution")
plt.legend()
plt.show()
