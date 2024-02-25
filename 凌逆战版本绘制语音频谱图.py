import wave
import matplotlib.pyplot as plt
import numpy as np
wave_path = r'D:\Users\Snake Konginchrist\Desktop\不常用软件及文档\福州大学校歌 00_02_37-00_02_54.wav'
f = wave.open(wave_path, "rb")
# f = wave.open(r"C:\Windows\media\Windows Background.wav", "rb")
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
strData = f.readframes(nframes)  # 读取音频，字符串格式
waveData = np.fromstring(strData, dtype=np.int16)  # 将字符串转化为int
waveData = waveData*1.0/(max(abs(waveData)))  # wave幅值归一化
waveData = np.reshape(waveData, [nframes, nchannels]).T
f.close()

plt.specgram(waveData[0], Fs=framerate, scale_by_freq=True, sides='default')
plt.ylabel('Frequency(Hz)')
plt.xlabel('Time(s)')
plt.show()
# def plot_fft_freq_chart(wave_path,plot=False):
#     y = np.zeros(nframes)
#
#     for i in range(nframes):
#         val = file.readframes(nframes)
#         left = val[0:2]
#         # right = val[2:4]
#         v = struct.unpack('h', left)[0]
#         y[i] = v
#
#     Fs = framerate
#     try:
#         data, freqs, bins, im = np.specgram(y, NFFT=1024, Fs=Fs, noverlap=900)
#         mm = data[127]
#         mm = 10. * np.log10(mm + 1e-4)
#
#     except Exception as e:
#         print("error is: ", e)
#         return -50
#
#     freq1khz_value = np.mean(mm)
#     print(freq1khz_value)
#     if pl.plot:
#         pl.show()
#         return freq1khz_value
# plot_fft_freq_chart(wave_path, True)
