import matplotlib.pylab as plt
import mqam_bp 
import numpy as np

msg = np.array([1, 1, 0, 1, 1, 0, 1, 1])


mod = mqam_bp.MQAM()

a=mod.modulation(msg,4)
plt.plot(a)
plt.show()