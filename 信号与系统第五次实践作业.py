import wave
import numpy as np
import pylab as pl
import pyaudio
wave_path = r'D:\Users\Snake Konginchrist\Desktop\不常用软件及文档\福州大学校歌 00_02_37-00_02_54.wav'
file = wave.open(wave_path, "rb")
params = file.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
str_data = file.readframes(nframes)  # 读音频，字符串格式
file.close()
wave_data = np.fromstring(str_data, dtype=np.short)
wave_data.shape = -1, 2
wave_data = wave_data.T
time = np.arange(0, nframes) * (1.0 / framerate)
pl.subplot(211)
pl.plot(time, wave_data[0], linewidth=1)
pl.grid('on')
pl.subplot(212)
pl.plot(time, wave_data[1], c="g")
pl.xlabel("Time (seconds)", fontsize=16)
pl.ylabel("Amplitude", fontsize=16)
pl.grid('on')
pl.show()
print("nchannels:", nchannels)  # 通道数
print("sampwidth:", sampwidth)  # 采样字节长度
print("framerate:", framerate)  # 采样频率
print("nframes:", nframes, "\n")  # 音频总帧数(数据总长)
# CHUNK = 1024
p = pyaudio.PyAudio()  # 获得语音文件的各个参数
WIDTH = file.getsampwidth()
FORMAT = p.get_format_from_width(file.getsampwidth())
CHANNELS = file.getnchannels()
RATE = file.getframerate()
print('WIDTH:{} \nFORMAT: {} \nCHANNELS: {} \nRATE: {}'.format(WIDTH, FORMAT, CHANNELS, RATE))
# 该段“福州大学校歌”音频默认情况下WIDTH=2, FORMAT=8, CHANNELS=2, RATE=48000



# 绘制频域图
def plot_freqdomain(start, fft_size):
    # 获取wave数据，获取帧率数据，ffz_size是我们的采样频率
    # 1.取出所需部分进行傅里叶变换，并得到幅值，rfft，对称保留一半，结果为 fft_size/2-1 维复数数组
    fft_y1 = np.fft.rfft(wave_data[0][start:start + fft_size - 1]) / fft_size  # 左声部
    fft_y2 = np.fft.rfft(wave_data[1][start:start + fft_size - 1]) / fft_size  # 右声部
    # 2.计算频域图x值，最值为0Hz，最大值一般设为采样频率的一半
    freqs = np.linspace(0, framerate//2, fft_size//2)
    pl.subplot(211)
    pl.plot(freqs, np.abs(fft_y1))
    pl.xlabel("Frequency(Hz):Left")
    pl.ylabel("Amplitude")
    pl.subplot(212)
    pl.plot(freqs, np.abs(fft_y2), c='g')
    pl.xlabel("Frequency(Hz):Right")
    pl.ylabel("Amplitude")
    pl.show()


def play():  # 打开音频流， output=True表示音频输出
    # WIDTH = 4
    # FORMAT = 8
    # CHANNELS = 1
    RATE = 64000  # 可以在这里更改音频的参数，在这里我改了采样频率
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)
# frames_per_buffer=CHUNK)
# play stream (3) frames_per_buffer=CHUNK, 按照1024的块读取音频数据到音频流，并播放
# while len(str_data) > 0:# 该句旨在循环播放，我不想循环播放，所以注释掉了
    stream.write(str_data)
# data = file.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
    file.close()
    p.terminate()


plot_freqdomain(0, 100000)
play()
