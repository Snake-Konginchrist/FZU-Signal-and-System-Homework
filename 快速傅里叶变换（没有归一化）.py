import numpy as np
# from numpy import fft
# 这句跟下一句功能上是一样的，不知道为什么会报错 TypeError: 'module' object is not callable
from scipy.fftpack import fft
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
mpl.rcParams['axes.unicode_minus'] = False  # 显示负号

# 采样点选择1400个，因为设置的信号频率分量最高为600赫兹，根据采样定理知采样频率要大于信号频率2倍，所以这里设置采样频率为1400赫兹（即一秒内有1400个采样点，一样意思的）
x = np.linspace(0, 1, 1400)
# 设置需要采样的信号，频率分量有200，400和600
y = 7 * np.sin(2 * np.pi * 200 * x) + \
    5 * np.sin(2 * np.pi * 400 * x) + \
    3 * np.sin(2 * np.pi * 600 * x)
plt.figure()
plt.title('原始波形')
plt.plot(x, y)

plt.figure()
plt.title('原始部分波形（前50组样本）')
plt.plot(x[0:50], y[0:50])
plt.show()

fft_y = fft(y)  # 快速傅里叶变换
print(len(fft_y))
print(fft_y[0:10])

N = 1400
x = np.arange(N)  # 频率个数

abs_y = np.abs(fft_y)  # 取复数的绝对值，即复数的模(双边频谱)
angle_y = np.angle(fft_y)  # 取复数的角度

plt.figure()
plt.plot(x, abs_y)
plt.xlabel('频率')
plt.ylabel('幅度')
plt.title('双边振幅谱（未归一化）')

plt.figure()
plt.plot(x, angle_y)
plt.xlabel('频率')
plt.ylabel('角度')
plt.title('双边相位谱（未归一化）')
plt.show()
