from numpy import mgrid,sin,cos,pi,array,exp
from matplotlib.pyplot import plot,show,title,legend,xlabel,ylabel
x = mgrid[0:10:0.02]
def sine():# 设角频率Ω=pi
    y= sin(pi*x)
    plot(x, y, 'blue', linewidth=0.6)
    title('sine')
    xlabel('Time')
    ylabel('Amplitude')
    show()
def sine_Fourier():
    y = 0
    for i in range(-10, 10, 1):
        if i==1:
            y0 = pi*sin(i*pi*x)
        if i==-1:
            y1 = -pi*sin(i*pi*x)
    y = y0 + y1
    plot(x, y, 'blue', linewidth=0.6)
    title('sine_Fourier')
    xlabel('Time')
    ylabel('Amplitude')
    show()

sine()
sine_Fourier()