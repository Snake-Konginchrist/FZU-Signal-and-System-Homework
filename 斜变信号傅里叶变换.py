from numpy import mgrid,sin,cos,pi,array,exp
from matplotlib.pyplot import plot,show,title,legend,xlabel,ylabel
x = mgrid[0:10:0.02]
def unit_ramp():
    y = x
    plot(x, y, 'red', linewidth=0.6)
    title('unit_ramp')
    xlabel('Time')
    ylabel('Amplitude')
    show()
def unit_ramp_Fourier():
    y = 0
    an= 0
    for i in range(1, 10000, 1):
        a0 = -2/(i**2)*cos(i*x)
        an=an+a0
    bn=2*pi*sin(0)
    y = an + bn  # 这种求和的方法是从C语言移植过来的
    plot(x, y, 'red', linewidth=0.6)
    title('unit_ramp_Fourier')
    xlabel('Time')
    ylabel('Amplitude')
    show()
unit_ramp()
unit_ramp_Fourier()