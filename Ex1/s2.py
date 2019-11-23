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
#Số tìu ý
n = 500
#Tiến hiệu s2(t)
def sin(x):
    sum = 0
    for i in range(0,2*n+1,1):
        sum = sum + A/math.pow(2*i+1, 2) * np.sin(2*math.pi*(2*i+1)*f*x)
    return sum
#Vẽ hình
plt.plot(t, sin(t))
plt.xlabel('t = 1/fs')
plt.ylabel('s2(t)')
plt.show()
