import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

fs1, clean = read("clean_audio.wav")
fs2, noisy = read("noisy_audio.wav")
fs3, periodic = read("periodic_audio.wav")

clean = clean.astype(np.float32) / 32768.0
noisy = noisy.astype(np.float32) / 32768.0
periodic = periodic.astype(np.float32) / 32768.0

auto_clean = np.correlate(clean, clean, mode='full')
auto_noisy = np.correlate(noisy, noisy, mode='full')
auto_periodic = np.correlate(periodic, periodic, mode='full')

print("Autocorrelation (Clean):", auto_clean)
print("Autocorrelation (Noisy):", auto_noisy)
print("Autocorrelation (Periodic):", auto_periodic)

cross_clean_noisy = np.correlate(clean, noisy, mode='full')
print("Cross-correlation (Clean vs Noisy):", cross_clean_noisy)

plt.figure(figsize=(12,10))

plt.subplot(4,1,1)
plt.plot(auto_clean)
plt.title("Autocorrelation - Clean Audio")

plt.subplot(4,1,2)
plt.plot(auto_noisy)
plt.title("Autocorrelation - Noisy Audio")

plt.subplot(4,1,3)
plt.plot(auto_periodic)
plt.title("Autocorrelation - Periodic Audio")

plt.subplot(4,1,4)
plt.plot(cross_clean_noisy)
plt.title("Cross-Correlation - Clean vs Noisy Audio")

plt.tight_layout()
plt.show()
