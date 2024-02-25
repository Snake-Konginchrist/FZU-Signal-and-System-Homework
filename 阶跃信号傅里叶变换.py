from numpy import mgrid,sin,cos,pi,array,exp
from matplotlib.pyplot import plot,show,title,legend,xlabel,ylabel
x = mgrid[0:10:0.1]
def unit_step():
    y= 1
    plot(x, y, 'black', linewidth=0.6)
    title('unit_step')
    xlabel('Time')
    ylabel('Amplitude')
    show()
def unit_step_Fourier():
    a0=0.5
    bn=0
    an = 2 * pi * cos(0 * pi * x)
    for i in range(0,100,1):
        if i==0:
            continue
        b1=2/i*sin(i*pi*x)
        bn=bn+b1
    y=a0+an+bn
    plot(x, y, 'black', linewidth=0.6)
    title('unit_step_Fourier')
    xlabel('Time')
    ylabel('Amplitude')
    show()
unit_step()
unit_step_Fourier()