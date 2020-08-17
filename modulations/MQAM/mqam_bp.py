from commpy.modulation import QAMModem
import numpy as np
import matplotlib.pyplot as plt
import math

class MQAM:

  def modulation(self,msg,M):
    qam = QAMModem(M)
    qam_constellation=qam.modulate(msg)

    qam_real = qam_constellation.real
    qam_img = qam_constellation.imag

    bp=0.000001 #bit period
    sp=bp*2    #symbol period for M-array QAM
    sr=1/sp    #symbol rate
    f=sr*2     #carry frequency 

    t=np.arange(sp/100, sp, sp/100)
    ss=len(t)

    m = []
    for k  in range(0,len(qam_real)):
        yr=qam_real[k]*np.cos(2*math.pi*f*t)                   # inphase or real component
        yim=qam_img[k]*np.sin(2*math.pi*f*t)           # Quadrature or imagenary component 
        y=[a + b for a, b in zip(yr, yim)]
        m = m+y
    
    #m = awgn(m,snr);
    return m