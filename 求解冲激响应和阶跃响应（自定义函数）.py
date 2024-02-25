# 自定义step_plot()
import numpy as np
import control as ctl
import matplotlib.pyplot as plt


def step_plot(s):
    y, t = ctl.step_response(s)
    plt.plot(y, t, 'b', linewidth=1.5)
    plt.title('Step Response', fontsize=16)
    plt.xlabel('Time(seconds)', fontsize=12)
    plt.ylabel('Amplitude', fontsize=12)
    plt.show()


def impulse_plot(s):
    y, t = ctl.impulse_response(s)
    plt.plot(y, t, 'b', linewidth=1.5)
    plt.title('Impulse Response', fontsize=16)
    plt.xlabel('Time(seconds)', fontsize=12)
    plt.ylabel('Amplitude', fontsize=12)
    plt.show()


s = ctl.tf([4], [1, 2, 10, 8])
step_plot(s)
impulse_plot(s)
