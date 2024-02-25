# coding=gbk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl


# ���ݿ��ٸ���Ҷ�㷨�õ��źŵ�Ƶ��
def test_fft():
    sampling_rate = 8000  # ������
    fft_size = 8000  # FFT����
    t = np.arange(0, 1.0, 1.0 / sampling_rate)
    x = np.sin(2 * np.pi * 156.25 * t) + 2 * np.sin(2 * np.pi * 234.375 * t) + 3 * np.sin(2 * np.pi * 200 * t)
    xs = x[:fft_size]

    xf = np.fft.rfft(xs) / fft_size  # ����fft_size/2+1 ��Ƶ��

    freqs = np.linspace(0, sampling_rate / 2, fft_size / 2 + 1)  # ��ʾƵ��
    xfp = np.abs(xf) * 2  # �����źŵķ�ֵ�������

    plt.figure(num='original', figsize=(15, 6))
    plt.plot(x[:100])

    plt.figure(figsize=(8, 4))
    plt.subplot(211)
    plt.plot(t[:fft_size], xs)
    plt.xlabel(u"ʱ��(��)", fontproperties='FangSong')
    plt.title(u"156.25Hz��234.375Hz�Ĳ��κ�Ƶ��", fontproperties='FangSong')

    plt.subplot(212)
    plt.plot(freqs, xfp)
    plt.xlabel(u"Ƶ��(Hz)", fontproperties='FangSong')
    plt.ylabel(u'��ֵ', fontproperties='FangSong')
    plt.subplots_adjust(hspace=0.4)
    plt.show()


test_fft()
# np.clip(a, a_min, a_max, out) �����a ��shapeһ�������ڵ���a_min��С�ڵ���a_max���������� [a_min, a_max]֮�����
a = np.arange(10)
print(a)
print(a.shape)
# [0 1 2 3 4 5 6 7 8 9]
b = np.empty((10,))
np.clip(a, 3, 8, out=b)
print(b)
# [3. 3. 3. 3. 4. 5. 6. 7. 8. 8.]
c = np.clip(a, 4, 10)
print(c)
# [4 4 4 4 4 5 6 7 8 9]
# a_min�� a_maxҲ����������a ��ͬshape������
d = np.arange(4)
d1 = np.clip(d, [-1, 1, -3, 2], 2)
print(d)
print(d1)
# [0 1 2 3] #ԭ����
# [0 1 2 2]

print(np.log10(1000))


def test_fft():
    # FFT�任�����һ����ֵ��������ģ��������ĳ���N������2���������ݣ�����64, 128, 256�ȵȣ� ��ֵ������ʵ��Ҳ�����Ǹ�����
    # ͨ�����ǵ�ʱ���źŶ���ʵ����������涼��ʵ��Ϊ�������ǿ��԰���һ��ʵ������ɶ�ĳ�������źŰ���һ��ȡ�����ڽ���ȡ����������
    # ���������N��ʵ��ֵ����FFT�任�����õ�һ����N�����������飬���ǳƴ˸�������ΪƵ���źţ��˸�������������¹��ɣ�
    #
    # �±�Ϊ0��N/2��������������������Ϊ0��
    # �±�Ϊi��N-i�������������Ҳ����������������ֵ��ͬ�������෴��
    np.random.seed(66)
    x = np.random.rand(8)
    print(x)
    #  [0.15428758 0.13369956 0.36268547 0.67910888 0.19445006 0.25121038
    # 0.75841639 0.55761859]
    xf = np.fft.fft(x)
    print(xf)
    #  [ 3.0914769 +0.j   -0.20916178+0.39291702j -0.77236422+0.85181752j
    #  0.12883683-0.39854483j -0.15179792+0.j   0.12883683+0.39854483j
    #  -0.77236422-0.85181752j -0.20916178-0.39291702j]
    # ͨ�����ٸ���Ҷ�任����任 ifft ��ԭ��ԭ����ֵ
    x1 = np.fft.ifft(xf)
    print(x1)
    # [0.15428758+0.00000000e+00j 0.13369956-2.00387919e-16j
    # 0.36268547+1.66533454e-16j 0.67910888+1.51815661e-16j
    # 0.19445006+0.00000000e+00j 0.25121038-1.51815661e-16j
    # 0.75841639-1.66533454e-16j 0.55761859+2.00387919e-16j]
    # ����������������FFT�任֮�����Щ����������ʲô��˼��
    # �����±�Ϊ0��ʵ����ʾ��ʱ���ź��е�ֱ���ɷֵĶ���
    # �±�Ϊi�ĸ���a+b*j��ʾʱ���ź�������ΪN/i��ȡ��ֵ�����Ҳ������Ҳ��ĳɷֵĶ��٣� ����a��ʾcos���εĳɷ֣�b��ʾsin���εĳɷ�
    x = np.ones(8)
    x2 = np.fft.fft(x) / len(x)  # Ϊ�˼�������ɷֵ��������٣���Ҫ��FFT�Ľ������FFT�ĳ���
    print(x2)
    # [1.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
    x = np.arange(0, 2 * np.pi, 2 * np.pi / 8)
    y = np.sin(x)
    x3 = np.fft.fft(y) / len(y)
    print(x3)
    # [ 1.43029718e-18+0.00000000e+00j -4.44089210e-16-5.00000000e-01j # ֻ���±�Ϊ 1 �ĸ������鲿Ϊ-0.5��
    # 1.53080850e-17-1.38777878e-17j 3.87727691e-17-1.11022302e-16j
    # 2.91858728e-17+0.00000000e+00j 0.00000000e+00-1.11022302e-16j
    # 1.53080850e-17+1.38777878e-17j 3.44084101e-16+5.00000000e-01j]
    output1 = np.fft.fft(np.cos(x) / len(x))
    print(output1)
    # [-4.30636606e-17+0.00000000e+00j 5.00000000e-01-2.66538563e-16j #ֻ���±�Ϊ1 ��ʵ��Ϊ 0.5
    # 1.53080850e-17+0.00000000e+00j 5.55111512e-17+1.97149624e-16j
    # 1.24474906e-17+0.00000000e+00j -1.11022302e-16+2.05306223e-16j
    # 1.53080850e-17+0.00000000e+00j 5.00000000e-01-1.35917284e-16j]
    # �ۺϵ�����
    x = np.arange(0, 2 * np.pi, 2 * np.pi / 128)
    y = 0.3 * np.cos(x) + 0.5 * np.cos(2 * x + np.pi / 4) + 0.8 * np.cos(3 * x - np.pi / 3)
    yf = np.fft.fft(y) / len(y)
    print(2 * np.abs(yf[1]), np.rad2deg(np.angle(yf[1])))
    #  0.30000000000000016 3.3130777931911615e-15   #�������ֵ����λ��
    print(2 * np.abs(yf[2]), np.rad2deg(np.angle(yf[2])))
    #  0.5000000000000002 44.999999999999986
    print(2 * np.abs(yf[3]), np.rad2deg(np.angle(yf[3])))
#  0.7999999999999998 -60.00000000000007
# ����Ϊ128/1.0������Ҳ�����λΪ0�� ���Ϊ0.3
# ����Ϊ64/2.0������Ҳ�����λΪ45�ȣ� ���Ϊ0.5
# ����Ϊ128/3.0������Ҳ�����λΪ-60�ȣ����Ϊ0.8
# test_fft()
# ʹ�ö���������ϳ����ǲ�
# ȡFFT����Ľ��freqs�е�ǰn����кϳɣ����غϳɽ��������loops�����ڵĲ���
def fft_combine(freqs, n, loops=1):
    length = len(freqs) * loops
    data = np.zeros(length)
    index = loops * np.arange(0, length, 1.0) / length * (2 * np.pi)
    for k, p in enumerate(freqs[:n]):
        if k != 0:
            p *= 2  # ��ȥֱ���ɷ�֮�⣬�����ϵ����*2
        data += np.real(p) * np.cos(k * index)  # ���ҳɷֵ�ϵ��Ϊʵ����
        data -= np.imag(p) * np.sin(k * index)  # ���ҳɷֵ�ϵ��Ϊ����������
    return index, data
# ����size��ȡ�������ǲ���������Ϊ1
def triangle_wave(size):
    x = np.arange(0, 1, 1.0 / size)
    y = np.where(x < 0.5, x, 0)
    y = np.where(x >= 0.5, 1 - x, y)
    return x, y


def test_show():
    fft_size = 256
    # �������ǲ�����FFT
    x, y = triangle_wave(fft_size)
    fy = np.fft.fft(y) / fft_size
    # �������ǲ���FFT��ǰ20�����������ڲ����±�Ϊż����ֵ��Ϊ0�� ���ȡ
    # log֮������С���޷���ͼ����np.clip������������ֵ�������ޣ���֤��ͼ��ȷ
    pl.figure()
    pl.plot(np.clip(20 * np.log10(np.abs(fy[:20])), -120, 120), "o")
    pl.xlabel("frequency bin")
    pl.ylabel("power(dB)")
    pl.title("FFT result of triangle wave")
    # ����ԭʼ�����ǲ��������Ҳ��𼶺ϳɵĽ����ʹ��ȡ����Ϊx������
    pl.figure()
    pl.plot(y, label="original triangle", linewidth=2)
    for i in [0, 1, 3, 5, 7, 9]:
        index, data = fft_combine(fy, i + 1, 2)  # �����������ڵĺϳɲ���
        pl.plot(data, label="N=%s" % i)
    pl.legend()
    pl.title("partial Fourier series of triangle wave")
    pl.show()

# test_show()
