import matplotlib.pylab as plt
import mqam_bp 
import numpy as np
from commpy.channels import awgn

msg = np.array([1, 1, 0, 1, 1, 0, 1, 1])
snr=-10

mod = mqam_bp.MQAM()

a=mod.modulation(msg,4)
plt.plot(awgn(a,snr))
plt.show()