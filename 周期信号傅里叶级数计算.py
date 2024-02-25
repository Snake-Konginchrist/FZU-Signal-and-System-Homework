from numpy import *
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
mpl.rcParams['axes.unicode_minus'] = False  # 显示负号
# x = mgrid[0:10:0.02]
# t = linspace(0, 10, 1000)
# Ω = linspace(0, 10, 20)  # 连续的频率
k = arange(0, 30)  # 离散的角频率，准确来说是谐波的次数
seterr(divide='ignore', invalid='ignore')  # 避免使用numpy时出现了0除以0的情况造成报错

def fourierseries(n):
    return 1/3*((2*(1-exp(-8j*pi*n/3))/(2j*n*pi/3))+(exp(-2*(2j*n*pi/3+1))-1)/((2j*pi*n/3)+1))

def spectrum():
    fn = fourierseries(k)
    f = abs(fn)
    phase = angle(fn)
    plt.show()
    plt.figure(figsize=(10, 12))
    plt.subplot(211)
    plt.title('幅度谱', fontsize=16)
    plt.stem(k, f, 'b')  # 绘制棉棒图
    plt.ylabel('幅度', fontsize=14)
    plt.subplot(212)
    plt.title('相位谱', fontsize=16)
    plt.stem(k, phase, 'g')
    plt.xlabel('谐波次数（角频率=谐波次数*基波角频率）', fontsize=12)
    plt.ylabel('相位', fontsize=14)
    plt.show()

spectrum()

# def signal2():
#     y = 4/3+(exp(-4)-1)/6
#     for i in range(1, 1000, 1):
#         y0 = fourierseries(2*pi*i/3)*exp(2j*pi*x*i/3)
#         y = y+y0
#     plt.plot(x, y, 'blue', linewidth=1.5)
#     plt.title('''Signal2's Waveform''')
#     plt.xlabel('Time')
#     plt.ylabel('Amplitude')
#     plt.show()
#
# signal2()
# def fourier_transform():
#     global FΩ
#     x = symbols('x')
#     FΩ = integrate(((2-np.exp(-2*x))*complex(cos(x),-sin(x)*j)), (x, 0, 2))
#     a0 = (1-exp(-pi))/pi+1
#     y = a0 / 2
#     for i in range(1, 100, 1):
#         s0 = ((1-(-1)**i*exp(-pi))/(pi*(1+i**2))*cos(i*x) +
#               1/pi*((-i*(1-(-1)**i*exp(-pi)))/(1+i**2) + (1-(-1)**i)/i) * sin(i*x))
#         FΩ = FΩ + s0
#     return FΩ

# signal1(t)
# plt.ylim(-0.5, 2.5)
# plt.title('Signal1:f1(t)=(2-e^-2t)u(t)')
# plt.xlabel('Time')
# plt.ylabel('Amplitude')
# plt.plot(t, y1, 'red', linewidth=1.0)
# plt.show()
#
# fourier_transform()
# plt.xlabel('Frequency')
# plt.ylabel('Amplitude')
# plt.plot(x, y, 'orange', linewidth=1.0)
# plt.title('Fourier Transform of Signal1')
# plt.show()
# plt.ylim(0, 2.5)
# plt.plot(Ω, f, 'red', linewidth=1.6)
# plt.title('''Signal2's Spectrum''')
# plt.xlabel('Frequency')
# plt.ylabel('Amplitude')
