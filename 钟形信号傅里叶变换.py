from numpy import mgrid,sin,cos,pi,array,exp
from matplotlib.pyplot import plot,show,title,legend,xlabel,ylabel
import math
x = mgrid[-10:10:0.02]
def Gauss():#设钟形信号的E为1，t也为1
    y= exp(-x**2)
    plot(x, y, 'purple', linewidth=0.6)
    title('Gauss')
    xlabel('Time')
    ylabel('Amplitude')
    show()
def Gauss_Fourier():
    y=0
    for i in range(0,100,1):
        y0=math.sqrt(pi)*exp(-(i/2)**2)*cos(i*pi*x)
        y=y+y0
    plot(x, y, 'purple', linewidth=0.6)
    title('Gauss_Fourier')
    xlabel('Time')
    ylabel('Amplitude')
    show()
Gauss()
Gauss_Fourier()