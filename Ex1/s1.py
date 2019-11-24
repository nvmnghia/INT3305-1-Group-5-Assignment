import matplotlib.pyplot as plt
import numpy as np
import math

#Tần số lấy mẫu
fs = 1000
#Thời gian đo
t = np.arange(-1, 1, 1/fs)
#Biên độ tín hiệu
A = 100
#Tần số cơ bản
f = 5
#Tiến hiệu s1(t)
s1 = A * np.sin(2 * math.pi * f * t)
#Vẽ hình
plt.plot(t, s1)
plt.title('s1(t) = Asin(2πft)')
plt.xlabel('t = 1/fs')
plt.ylabel('s1(t)')
plt.show()