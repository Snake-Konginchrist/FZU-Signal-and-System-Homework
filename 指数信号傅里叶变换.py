from numpy import mgrid,sin,cos,pi,array,exp
from matplotlib.pyplot import plot,show,title,legend,xlabel,ylabel
x = mgrid[-10:10:0.02]
def exponent():
    y= exp(-x)
    plot(x, y, 'black', linewidth=0.6)
    title('exponent')
    xlabel('Time')
    ylabel('Amplitude')
    show()
def exponent_Fourier():
    y=0
    for i in range(0,100,1):
        y0=2/(1+i**2)*cos(i*pi*x)+(2*i)/(1+i**2)*sin(i*pi*x)
        y=y+y0
    plot(x, y, 'black', linewidth=0.6)
    title('exponent_Fourier')
    xlabel('Time')
    ylabel('Amplitude')
    show()
exponent()
exponent_Fourier()
