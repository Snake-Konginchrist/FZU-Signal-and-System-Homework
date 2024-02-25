import wave
import data as data
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import librosa

path = r'D:\Users\Snake Konginchrist\Desktop\福州大学校歌 00_02_37-00_02_54.wav'
librosa.load(path, sr=22050, mono=True, offset=0.0, duration=None)