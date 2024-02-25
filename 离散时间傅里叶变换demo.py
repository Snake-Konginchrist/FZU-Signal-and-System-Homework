# 离散时间傅里叶变换的 python 实现
import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 5000
t1 = np.arange(0, 10.0, 1.0/sampling_rate)
x1 = np.where((t1 > 0) & (t1 < 2), 2-np.exp(-2*t1), 0)
# 傅里叶变换
def fft1(xx):
#   t=np.arange(0, s)
  t = np.linspace(0, 1.0, len(xx))
  f = np.arange(len(xx)/2+1, dtype=complex)
  for index in range(len(f)):
    f[index] = complex(np.sum(np.cos(2*np.pi*index*t)*xx), -np.sum(np.sin(2*np.pi*index*t)*xx))
  return f
# len(x1)
xf = fft1(x1)/len(x1)
freqs = np.linspace(0, sampling_rate//2, len(x1)//2+1)
plt.figure(figsize=(16, 4))
plt.plot(freqs, 2*np.abs(xf), 'b--')

plt.xlabel("Frequency(Hz)")
plt.ylabel("Amplitude($m$)")
plt.title("Amplitude-Frequency Curve")

plt.show()
plt.figure(figsize=(16, 4))
plt.plot(freqs, 2*np.abs(xf), 'g--')

plt.xlabel("Frequency(Hz)")
plt.ylabel("Amplitude($m$)")
plt.title("Amplitude-Frequency curve")
plt.xlim(0, 20)
plt.show()