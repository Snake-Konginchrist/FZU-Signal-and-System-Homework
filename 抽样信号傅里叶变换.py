from numpy import mgrid,sin,cos,pi,array,exp
from matplotlib.pyplot import plot,show,title,legend,xlabel,ylabel
x = mgrid[-10:10:0.02]
def sample():
    y= sin(pi*x)/(pi*x)
    plot(x, y, 'black', linewidth=0.6)
    title('sample')
    xlabel('Time')
    ylabel('Amplitude')
    show()
def sample_Fourier():
    y = 0
    for i in range(0, 10, 1):
        y0 = 2*cos(i*pi*x)
        y = y + y0  # 这种求和的方法是从C语言移植过来的
    y=y+0.5
    plot(x, y, 'red', linewidth=0.6)
    title('sample_Fourier')
    xlabel('Time')
    ylabel('Amplitude')
    show()

sample()
sample_Fourier()