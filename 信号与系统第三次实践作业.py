import numpy as np
# from numpy import fft
# 这句跟下一句功能上是一样的，不知道为什么会报错 TypeError: 'module' object is not callable
from scipy.fftpack import fft
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
mpl.rcParams['axes.unicode_minus'] = False  # 显示负号
t = np.linspace(-4, 4, 1000)

def signal1(t):
    return np.where((t > 0) & (t < 2), 2-np.exp(-2*t), 0)

def fourier_transform(t):
    global fft_y, half_t, abs_y, angle_y, normalization_y, normalization_half_y
    fft_y = fft(signal1(t))  # 快速傅里叶变换
    N = 100
    t = np.arange(N)  # 频率个数
    half_t = t[range(int(N / 2))]  # 取一半区间
    abs_y = np.abs(fft_y)  # 取复数的绝对值，即复数的模(双边频谱)
    angle_y = np.angle(fft_y)  # 取复数的角度
    normalization_y = abs_y / N  # 归一化处理（双边频谱）
    normalization_half_y = normalization_y[range(int(N / 2))]  # 由于对称性，只取一半区间（单边频谱）

signal1(t)
fourier_transform(t)

plt.subplot(311)
plt.plot(t, signal1(t), linewidth=1.5)
plt.title('原始波形',fontsize=16)
#plt.show()
'''
plt.subplot(232)
plt.plot(t, fft_y, 'green')
plt.title('双边振幅谱(未求振幅绝对值)', fontsize=9, color='green')

plt.subplot(233)
plt.plot(t, abs_y, 'blue')
plt.title('双边振幅谱(未归一化)', fontsize=9, color='blue')

# plt.subplot(235)
plt.plot(t, normalization_y, 'orange')
plt.title('双边振幅谱(归一化)', fontsize=16, color='orange')
plt.show()'''
# plt.figure(figsize=(12, 10))
plt.subplot(312)
plt.plot(half_t, normalization_half_y, 'red')
plt.title('单边振幅谱(归一化)', fontsize=16, color='red')
#plt.show()
plt.subplot(313)
plt.plot(t, angle_y, 'black',linewidth=0.1)
plt.title('双边相位谱(未归一化)', fontsize=16, color='black')
plt.show()
