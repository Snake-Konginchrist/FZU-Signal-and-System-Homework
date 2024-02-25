import matplotlib.pyplot as plt
from pylab import *
x = mgrid[-10:10:0.02]  # 这里类似于MATLAB用冒号产生步长为0.02的序列，但是语法和MATLAB不同
n = arange(1, 1000)


def fourier_transform():
    global y
    a0 = (1-exp(-pi))/pi+1
    y = a0 / 2
    for i in range(1, 100, 1):
    # s0 = ((1-(-1)**i*exp(-pi))/(pi*(1+i**2))*cos(i*x)+1/pi*((-i*(1-(-1)**i*exp(-pi)))/(1+i**2) + (1-(-1)**i)/i) * sin(i*x))
        y = y + s0


fourier_transform()
plt.plot(x, y, 'orange', linewidth=1.0)
plt.title('Fourier_Transform')
plt.show()
