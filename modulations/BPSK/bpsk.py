import numpy as np
import matplotlib.pylab as plt
import scipy.signal as signal



class BPSK:

    def modulation(self,msg): 

        #codificador non-return-to-zero
        nrtn = 2*msg - 1 

        Tb = 1 # Tb representa a duração do bit
        Eb = 0.5 # Eb representa a energia por bit do sinal transmitido

        fc = 5 # frequencia da portadora, pode ser fc = n/Tb na qual n é um inteiro. Esta escolha de freqüência fc de portadora permite a
        #simulação de um sistema passa-faixa em um computador digital sem a necessidade de fc >> 1/Tb. (na qual 'n' é um inteiro)
        nb = msg.size #bits

        fs = 200 #frequência de amostragem
        n_amostras = nb*fs #numero de amostras

        t = np.linspace(0, nb, n_amostras) #sequência (n_amostras)

        array_fs = np.repeat(msg, fs)   # replicar cada bit fs vezes
        nrtn_fs = np.repeat(nrtn, fs) # replicar cada bit fs vezes (non-return-to-zero)

        #s(t)
        st = np.sqrt(2*Eb/Tb) * np.cos(2*np.pi * fc * t)
        #modulador de produto
        bpsk_s = nrtn_fs*st
        return bpsk_s

