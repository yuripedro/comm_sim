import numpy as np
from commpy.channels import awgn
import matplotlib.pylab as plt
import bpsk 

array = np.array([1, 1, 0, 1, 0])
snr=100

mod = bpsk.BPSK()

a=mod.modulation(array)
plt.plot(awgn(a,snr))
plt.show()