# 连续周期信号的傅立叶级数计算，三角函数形式
from sympy import cos, sin
from sympy.abc import t, n, y
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
# t = np.linspace(0, 10, 1000)
nf = 30  # nf的意思是频谱横坐标角频率的长度
T = 3
# tao = 1.0
an = np.zeros(nf)
bn = np.zeros(nf)
cn = np.zeros(nf)
phase = np.zeros(nf)
def signal1(t):
    return 2-np.exp(-2*t)
    # if (t > 0) and (t < 2):
    #     return 2-np.exp(-2*t)
    # else:
    #     return 0
    # return np.where((t > 0) & (t < 2), 2-np.exp(-2*t), 0)
# def fourierseries_trigonometric():
an[0] = integrate.quad(signal1(t), 0, T)/T
for n in range(1, nf):
    an[n] = 2/T*integrate.quad(lambda t: signal1(t)*cos(n*2*np.pi/T*t), 0, 2)
    bn[n] = 2/T*integrate.quad(lambda t: signal1(t)*sin(n*2*np.pi/T*t), 0, 2)
    cn[n] = np.sqrt(an[n]**2+bn[n]**2)
for i in range(0, nf):
    if an[i] >= 0:
        phase[i] = 0
    else:
        phase[i] = np.pi
k = np.arange(0, nf)
plt.subplot(211)
plt.title(u'幅度谱')
plt.stem(k, cn)  # 绘制棉棒图
plt.subplot(212)
plt.title(u'相位谱')
plt.stem(k, phase)
plt.show()
