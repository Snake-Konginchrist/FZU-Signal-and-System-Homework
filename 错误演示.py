import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(-2, 10, 1000)


def signal1(t):
    global y1
    y1 = np.where(t < 0, 0, 2-np.exp(-2*t))
    plt.ylim(-0.5, 2.5)
    plt.title('Signal1:f1(t)=(2-e^-2t)u(t)')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.plot(t, y1, 'red', linewidth=1.5)
    return y1


def signal2(t):
    global y2
    y2 = np.where((t > 0) & (t < 2), 1 + np.cos(np.pi * t), 0)
    plt.xlim(-1, 3)
    plt.ylim(-0.5, 2.5)
    plt.title('Signal2:f2(t)=(1+cosπt)[u(t)-u(t-2)]')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.plot(t, y2, 'blue', linewidth=1.5)
    return y2


def signal3(t):
    global y3
    y3 = signal1(2*t)-signal2(t)
    plt.title('Signal3:f1(2t)-f2(t)')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.plot(t, y3, 'black', linewidth=1.5)
    return y3


signal1(t)
plt.show()
signal2(t)
plt.show()
signal3(t)
plt.show()