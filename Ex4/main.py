from PIL import Image
import numpy as np
import scipy.fftpack as fp
from matplotlib import pylab

im2freq = lambda data: fp.rfft(fp.rfft(data, axis=0),
                               axis=1)
freq2im = lambda f: fp.irfft(fp.irfft(f, axis=1),
                                         axis=0)

data = np.array(Image.open('test.png'))

pylab.figure(figsize=(12,10))
freq2 = fp.fft2(data)
data_ = fp.ifft2(freq2).real
pylab.subplot(2,2,1), pylab.imshow(data, cmap='gray'), pylab.title('original image', size = 20)
pylab.subplot(2,2,2), pylab.imshow(20*np.log10( 0.01 + np.abs(fp.fftshift(freq2))), cmap='gray')
pylab.title('FFT Spectrum Magnitude', size = 20)
pylab.subplot(2,2,3), pylab.imshow(np.angle(fp.fftshift(freq2)), cmap = 'gray')
pylab.title('FFT Phase', size = 20)
pylab.subplot(2,2,4), pylab.imshow(np.clip(data_, 0,255), cmap = 'gray')
pylab.title('Reconstructed Image', size = 20)
pylab.show()