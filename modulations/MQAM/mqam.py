import numpy as np
import math as mth
import codification as cod

class Modulations:

    def M_QAM(msg,M):

        ld=np.log2(M)
        ds=mth.ceil(ld)
        dif=ds-ld
        if dif!=0 :
            print("the value of M is only acceptable if log2(M) is an integer")    		
        
        nbit = len(msg)
        msg_reshape = np.reshape(msg,(int(ld),int(nbit/ld))).T
        
        #a = np.zeros([int(nbit/ld),int(ld)])
        for j in range(int(nbit/ld)):
            #for i in range(int(ld)):
            a=np.array_str(msg_reshape[j])
            print(a)
            #print(cod.Codification.bin2Dec(a[j],ld))

                #a=np.concatenate(msg_reshape[j,i])
                #
                #c[j] = str(msg_reshape[j,i])+str(msg_reshape[j,i])

        #for k in range(int(nbit/ld)):
        #print(msg_reshape[1])
        #print(cod.Codification.bin2Dec(,ld))
        
        #ass=as.T
        #print(cod.Codification.bin2Dec(a,ld))
        #print(a)
        return a
		