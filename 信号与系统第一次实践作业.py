# 完成斜变、指数、正弦、阶跃等任意一种波形的显示。
# 完成抽样信号或钟形（高斯）信号中任意一个波形的显示。
# 完成斜变、指数、正弦、阶跃等任意一种波形的傅里叶级数展开及波形合成。
# 完成抽样信号或钟形（高斯）信号中任意一个波形的傅里叶级数展开及波形合成。【玉洁七日】
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
    for i in range(0, 10, 1):
        y0 = (-1) ** (i) * cos((2 * i + 1) * x) / (2 * i + 1)
        y = y + y0  # 这种求和的方法是从C语言移植过来的
    plot(x, y, 'red', linewidth=0.6)
    title('unit_ramp_Fourier')
    xlabel('Frequency')
    ylabel('Amplitude')
    show()


def exponent():
    y= exp(-x)
    plot(x, y, 'orange', linewidth=0.6)
    title('exponent')
    xlabel('Time')
    ylabel('Amplitude')
    show()


def exponent_Fourier():
    y=0
    for i in range(0,10,1):
        y0=1/(1+i)*exp(i*x)
        y=y+y0
    plot(x, y, 'purple', linewidth=0.6)
    title('exponent_Fourier')
    xlabel('Frequency')
    ylabel('Amplitude')
    show()


def sine():
    y= sin(x)
    plot(x, y, 'blue', linewidth=0.6)
    title('sine')
    xlabel('Time')
    ylabel('Amplitude')
    show()


def sine_Fourier():
    y = 0
    for i in range(0, 10, 1):
        y0 = 1 / (1+i) * exp(i * x)
        y = y + y0
    plot(x, y, 'black', linewidth=0.6)
    title('sine_Fourier')
    xlabel('Frequency')
    ylabel('Amplitude')
    show()


def unit_step():
    y = 1
    plot(x, y, 'green', linewidth=0.6)
    title('unit_step')
    xlabel('Time')
    ylabel('Amplitude')
    show()


unit_ramp()
exponent()
sine()
unit_ramp_Fourier()
exponent_Fourier()
sine_Fourier()
