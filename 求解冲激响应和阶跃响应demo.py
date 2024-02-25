from scipy.signal import lti, step2, impulse2
import matplotlib.pyplot as plt

s1 = lti([3], [1, 2, 0])    # 以分子分母的最高次幂降序的系数构建传递函数，s1=3/(s^2+2s+10）
s2 = lti([1], [1, 0.4, 0])   # s2=1/(s^2+0.4s+1)
s3 = lti([5], [1, 2, 0])     # s3=5/(s^2+2s+5)

t1, y1 = step2(s1)         # 计算阶跃输出，y1是Step response of system.
t2, y2 = step2(s2)
t3, y3 = step2(s3)
t11, y11 = impulse2(s1)
t22, y22 = impulse2(s2)
t33, y33 = impulse2(s3)

f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2,3,sharex='col',sharey='row') # 开启subplots模式
ax1.plot(t1, y1, 'r', label='s1 Step Response', linewidth=0.5)
ax1.set_title('s1 Step Response', fontsize=9)
ax2.plot(t2, y2, 'g', label='s2 Step Response', linewidth=0.5)
ax2.set_title('s2 Step Response', fontsize=9)
ax3.plot(t3, y3, 'b', label='s3 Step Response', linewidth=0.5)
ax3.set_title('s3 Step Response', fontsize=9)

ax4.plot(t11, y11, 'm', label='s1 Impulse Response', linewidth=0.5)
ax4.set_title('s1 Impulse Response', fontsize=9)
ax5.plot(t22, y22, 'y', label='s2 Impulse Response', linewidth=0.5)
ax5.set_title('s2 Impulse Response', fontsize=9)
ax6.plot(t33, y33, 'k', label='s3 Impulse Response', linewidth=0.5)
ax6.set_title('s3 Impulse Response', fontsize=9)

## plt.xlabel('Times')
## plt.ylabel('Amplitude')
# plt.legend()
plt.show()
