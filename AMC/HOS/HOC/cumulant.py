
import statistics as st

class Cumulant:
    
    def C20(self,r1,r2):
        y = st.mean([a * b for a, b in zip(r1, r2)])
        return y

    def C41(self,r1,r2,r3,r4):
        y = st.mean([a * b * c * d for a,b,c,d in zip(r1,r2,r3,r4)])-(self.C20(r1,r2) * self.C20(r3,r4) + self.C20(r1,r3) * self.C20(r2,r4) + self.C20(r2,r3) * self.C20(r1,r4) )
        return y


    def C60(self,r1,r2,r3,r4,r5,r6):
        c_12 = self.C20(r1, r2) 
        c_13 = self.C20(r1, r3) 
        c_14 = self.C20(r1, r4) 
        c_15 = self.C20(r1, r5) 
        c_16 = self.C20(r1, r6) 
        c_23 = self.C20(r2, r3) 
        c_24 = self.C20(r2, r4) 
        c_25 = self.C20(r2, r5) 
        c_26 = self.C20(r2, r6) 
        c_34 = self.C20(r3, r4) 
        c_35 = self.C20(r3, r5) 
        c_36 = self.C20(r3, r6) 
        c_45 = self.C20(r4, r5) 
        c_46 = self.C20(r4, r6) 
        c_56 = self.C20(r5, r6) 

        c_1234 = self.C41(r1, r2, r3, r4) 
        c_1235 = self.C41(r1, r2, r3, r5) 
        c_1236 = self.C41(r1, r2, r3, r6) 
        c_1245 = self.C41(r1, r2, r4, r5) 
        c_1246 = self.C41(r1, r2, r4, r6) 
        c_1256 = self.C41(r1, r2, r5, r6) 
        c_1345 = self.C41(r1, r3, r4, r5) 
        c_1346 = self.C41(r1, r3, r4, r6) 
        c_1356 = self.C41(r1, r3, r5, r6) 
        c_1456 = self.C41(r1, r4, r5, r6) 
        c_2345 = self.C41(r2, r3, r4, r5) 
        c_2346 = self.C41(r2, r3, r4, r6) 
        c_2356 = self.C41(r2, r3, r5, r6) 
        c_2456 = self.C41(r2, r4, r5, r6) 
        c_3456 = self.C41(r3, r4, r5, r6) 


        c_1234_56 = c_1234 * c_56 
        c_1235_46 = c_1235 * c_46 
        c_1236_45 = c_1236 * c_45 
        c_1245_36 = c_1245 * c_36 
        c_1246_35 = c_1246 * c_35 
        c_1256_34 = c_1256 * c_34 
        c_1345_26 = c_1345 * c_26 
        c_1346_25 = c_1346 * c_25 
        c_1356_24 = c_1356 * c_24 
        c_1456_23 = c_1456 * c_23 
        c_2345_16 = c_2345 * c_16 
        c_2346_15 = c_2346 * c_15 
        c_2356_14 = c_2356 * c_14 
        c_2456_13 = c_2456 * c_13 
        c_3456_12 = c_3456 * c_12 

        c_12_34_56 = c_12 * c_34 * c_56 
        c_13_24_46 = c_13 * c_24 * c_46 
        c_14_23_56 = c_14 * c_23 * c_56 
        c_12_35_46 = c_12 * c_35 * c_46 
        c_12_36_45 = c_12 * c_36 * c_45 
        c_13_25_46 = c_13 * c_25 * c_46 
        c_13_26_45 = c_13 * c_26 * c_45 
        c_15_23_46 = c_15 * c_23 * c_46 
        c_16_23_45 = c_16 * c_23 * c_45 
        c_14_25_36 = c_14 * c_25 * c_36 
        c_14_26_35 = c_14 * c_26 * c_35 
        c_15_24_36 = c_15 * c_24 * c_36 
        c_16_24_35 = c_16 * c_24 * c_35 
        c_15_26_34 = c_15 * c_26 * c_34 
        c_16_25_34 = c_16 * c_25 * c_34 



        y =  st.mean([a * b * c * d * e * f for a,b,c,d,e,f in zip(r1,r2,r3,r4,r5,r6)]) - ( c_1234_56 + c_1235_46 + c_1236_45 + c_1245_36 + c_1246_35 +  c_1256_34 + c_1345_26 + c_1346_25 + c_1356_24 + c_1456_23 + 
            c_2345_16 + c_2346_15 + c_2356_14 + c_2456_13 + c_3456_12  + 
            c_12_34_56 + c_13_24_46 + c_14_23_56 + c_12_35_46 + c_12_36_45 + 
            c_13_25_46 + c_13_26_45 + c_15_23_46 + c_16_23_45 + c_14_25_36 + 
            c_14_26_35 + c_15_24_36 + c_16_24_35 + c_15_26_34 + c_16_25_34 )

        return y


    def C80(self,r1,r2,r3,r4,r5,r6,r7,r8):
        c_12 = self.C20(r1, r2) 
        c_13 = self.C20(r1, r3) 
        c_14 = self.C20(r1, r4) 
        c_15 = self.C20(r1, r5) 
        c_16 = self.C20(r1, r6) 
        c_17 = self.C20(r1, r7) 
        c_18 = self.C20(r1, r8) 
        c_23 = self.C20(r2, r3) 
        c_24 = self.C20(r2, r4) 
        c_25 = self.C20(r2, r5) 
        c_26 = self.C20(r2, r6) 
        c_27 = self.C20(r2, r7) 
        c_28 = self.C20(r2, r8) 
        c_34 = self.C20(r3, r4) 
        c_35 = self.C20(r3, r5) 
        c_36 = self.C20(r3, r6) 
        c_37 = self.C20(r3, r7) 
        c_38 = self.C20(r3, r8) 
        c_45 = self.C20(r4, r5) 
        c_46 = self.C20(r4, r6) 
        c_47 = self.C20(r4, r7) 
        c_48 = self.C20(r4, r8) 
        c_56 = self.C20(r5, r6) 
        c_57 = self.C20(r5, r7) 
        c_58 = self.C20(r5, r8) 
        c_67 = self.C20(r6, r7) 
        c_68 = self.C20(r6, r8) 
        c_78 = self.C20(r7, r8) 


        c_1234 = self.C41(r1, r2, r3, r4) 
        c_1235 = self.C41(r1, r2, r3, r5) 
        c_1236 = self.C41(r1, r2, r3, r6) 
        c_1237 = self.C41(r1, r2, r3, r7) 
        c_1238 = self.C41(r1, r2, r3, r8) 
        c_1245 = self.C41(r1, r2, r4, r5) 
        c_1246 = self.C41(r1, r2, r4, r6) 
        c_1247 = self.C41(r1, r2, r4, r7) 
        c_1248 = self.C41(r1, r2, r4, r8) 
        c_1256 = self.C41(r1, r2, r5, r6) 
        c_1257 = self.C41(r1, r2, r5, r7) 
        c_1258 = self.C41(r1, r2, r5, r8) 
        c_1267 = self.C41(r1, r2, r6, r7) 
        c_1268 = self.C41(r1, r2, r6, r8) 
        c_1278 = self.C41(r1, r2, r7, r8) 
        c_1345 = self.C41(r1, r3, r4, r5) 
        c_1346 = self.C41(r1, r3, r4, r6) 
        c_1347 = self.C41(r1, r3, r4, r7) 
        c_1348 = self.C41(r1, r3, r4, r8) 
        c_1356 = self.C41(r1, r3, r5, r6) 
        c_1357 = self.C41(r1, r3, r5, r7) 
        c_1358 = self.C41(r1, r3, r5, r8) 
        c_1367 = self.C41(r1, r3, r6, r7) 
        c_1368 = self.C41(r1, r3, r6, r8) 
        c_1378 = self.C41(r1, r3, r7, r8) 
        c_1456 = self.C41(r1, r4, r5, r6) 
        c_1457 = self.C41(r1, r4, r5, r7) 
        c_1458 = self.C41(r1, r4, r5, r8) 
        c_1467 = self.C41(r1, r4, r6, r7) 
        c_1468 = self.C41(r1, r4, r6, r8) 
        c_1478 = self.C41(r1, r4, r7, r8) 
        c_1567 = self.C41(r1, r5, r6, r7) 
        c_1568 = self.C41(r1, r5, r6, r8) 
        c_1578 = self.C41(r1, r5, r7, r8) 
        c_1678 = self.C41(r1, r6, r7, r8) 
        c_2345 = self.C41(r2, r3, r4, r5) 
        c_2346 = self.C41(r2, r3, r4, r6) 
        c_2347 = self.C41(r2, r3, r4, r7) 
        c_2348 = self.C41(r2, r3, r4, r8) 
        c_2356 = self.C41(r2, r3, r5, r6) 
        c_2357 = self.C41(r2, r3, r5, r7) 
        c_2358 = self.C41(r2, r3, r5, r8) 
        c_2367 = self.C41(r2, r3, r6, r7) 
        c_2368 = self.C41(r2, r3, r6, r8) 
        c_2378 = self.C41(r2, r3, r7, r8) 
        c_2456 = self.C41(r2, r4, r5, r6) 
        c_2457 = self.C41(r2, r4, r5, r7) 
        c_2458 = self.C41(r2, r4, r5, r8) 
        c_2467 = self.C41(r2, r4, r6, r7) 
        c_2468 = self.C41(r2, r4, r6, r8) 
        c_2478 = self.C41(r2, r4, r7, r8) 
        c_2567 = self.C41(r2, r5, r6, r7) 
        c_2568 = self.C41(r2, r5, r6, r8) 
        c_2578 = self.C41(r2, r5, r7, r8) 
        c_2678 = self.C41(r2, r6, r7, r8) 
        c_3456 = self.C41(r3, r4, r5, r6) 
        c_3457 = self.C41(r3, r4, r5, r7) 
        c_3458 = self.C41(r3, r4, r5, r8) 
        c_3467 = self.C41(r3, r4, r6, r7) 
        c_3468 = self.C41(r3, r4, r6, r8) 
        c_3478 = self.C41(r3, r4, r7, r8) 
        c_3567 = self.C41(r3, r5, r6, r7) 
        c_3568 = self.C41(r3, r5, r6, r8) 
        c_3578 = self.C41(r3, r5, r7, r8) 
        c_3678 = self.C41(r3, r6, r7, r8) 
        c_4567 = self.C41(r4, r5, r6, r7) 
        c_4568 = self.C41(r4, r5, r6, r8) 
        c_4578 = self.C41(r4, r5, r7, r8) 
        c_4678 = self.C41(r4, r6, r7, r8) 
        c_5678 = self.C41(r5, r6, r7, r8) 

        c_123456 = self.C60(r1, r2, r3, r4, r5, r6) 
        c_123457 = self.C60(r1, r2, r3, r4, r5, r7) 
        c_123458 = self.C60(r1, r2, r3, r4, r5, r8) 
        c_123467 = self.C60(r1, r2, r3, r4, r6, r7) 
        c_123468 = self.C60(r1, r2, r3, r4, r6, r8) 
        c_123478 = self.C60(r1, r2, r3, r4, r7, r8) 
        c_123567 = self.C60(r1, r2, r3, r5, r6, r7) 
        c_123568 = self.C60(r1, r2, r3, r5, r6, r8) 
        c_123578 = self.C60(r1, r2, r3, r5, r7, r8) 
        c_123678 = self.C60(r1, r2, r3, r6, r7, r8) 
        c_124567 = self.C60(r1, r2, r4, r5, r6, r7) 
        c_124568 = self.C60(r1, r2, r4, r5, r6, r8) 
        c_124578 = self.C60(r1, r2, r4, r5, r7, r8) 
        c_124678 = self.C60(r1, r2, r4, r6, r7, r8) 
        c_125678 = self.C60(r1, r2, r5, r6, r7, r8) 
        c_134567 = self.C60(r1, r3, r4, r5, r6, r7) 
        c_134568 = self.C60(r1, r3, r4, r5, r6, r8) 
        c_134578 = self.C60(r1, r3, r4, r5, r7, r8) 
        c_134678 = self.C60(r1, r3, r4, r6, r7, r8) 
        c_135678 = self.C60(r1, r3, r5, r6, r7, r8) 
        c_145678 = self.C60(r1, r4, r5, r6, r7, r8) 
        c_234567 = self.C60(r2, r3, r4, r5, r6, r7) 
        c_234568 = self.C60(r2, r3, r4, r5, r6, r8) 
        c_234578 = self.C60(r2, r3, r4, r5, r7, r8) 
        c_234678 = self.C60(r2, r3, r4, r6, r7, r8) 
        c_235678 = self.C60(r2, r3, r5, r6, r7, r8) 
        c_245678 = self.C60(r2, r4, r5, r6, r7, r8) 
        c_345678 = self.C60(r3, r4, r5, r6, r7, r8) 

        c_123456_78 = c_123456 * c_78 
        c_123457_68 = c_123457 * c_68 
        c_123458_67 = c_123458 * c_67 
        c_123467_58 = c_123467 * c_58 
        c_123468_57 = c_123468 * c_57 
        c_123478_56 = c_123478 * c_56 
        c_1234_5678 = c_1234 * c_5678 
        c_1234_56_78 = c_1234 * c_56 * c_78 
        c_1234_57_68 = c_1234 * c_57 * c_68 
        c_1234_58_67 = c_1234 * c_58 * c_67 
        c_123567_48 = c_123567 * c_48 
        c_123568_47 = c_123568 * c_47 
        c_123578_46 = c_123578 * c_46 
        c_1235_4678 = c_1235 * c_4678 
        c_1235_46_78 = c_1235 * c_46 * c_78 
        c_1235_47_68 = c_1235 * c_47 * c_68 
        c_1235_48_67 = c_1235 * c_48 * c_67 
        c_123678_45 = c_123678 * c_45 
        c_1236_4578 = c_1236 * c_4578 
        c_1236_45_78 = c_1236 * c_45 * c_78 
        c_1237_4568 = c_1237 * c_4568 
        c_1238_4567 = c_1238 * c_4567 
        c_1237_45_68 = c_1237 * c_45 * c_68 
        c_1238_45_67 = c_1238 * c_45 * c_67 
        c_1236_47_58 = c_1236 * c_47 * c_58 
        c_1236_48_57 = c_1236 * c_48 * c_57 
        c_1237_46_58 = c_1237 * c_46 * c_58 
        c_1238_46_57 = c_1238 * c_46 * c_57 
        c_1237_48_56 = c_1237 * c_48 * c_56 
        c_1238_47_56 = c_1238 * c_47 * c_56 
        c_124567_38 = c_124567 * c_38 
        c_124568_37 = c_124568 * c_37 
        c_124578_36 = c_124578 * c_36 
        c_1245_3678 = c_1245 * c_3678 
        c_1245_36_78 = c_1245 * c_36 * c_78 
        c_1245_37_68 = c_1245 * c_37 * c_68 
        c_1245_38_67 = c_1245 * c_38 * c_67 
        c_124678_35 = c_124678 * c_35 
        c_1246_3578 = c_1246 * c_3578 
        c_1246_35_78 = c_1246 * c_35 * c_78 
        c_1247_3568 = c_1247 * c_3568 
        c_1248_3567 = c_1248 * c_3567 
        c_1247_35_68 = c_1247 * c_35 * c_68 
        c_1248_35_67 = c_1248 * c_35 * c_67 
        c_1246_37_58 = c_1246 * c_37 * c_58 
        c_1246_38_57 = c_1246 * c_38 * c_57 
        c_1247_36_58 = c_1247 * c_36 * c_58 
        c_1248_36_57 = c_1248 * c_36 * c_57 
        c_1247_38_56 = c_1247 * c_38 * c_56 
        c_1248_37_56 = c_1248 * c_37 * c_56 
        c_125678_34 = c_125678 * c_34 
        c_1256_3478 = c_1256 * c_3478 
        c_1256_34_78 = c_1256 * c_34 * c_78 
        c_1257_3468 = c_1257 * c_3468 
        c_1258_3467 = c_1258 * c_3467 
        c_1257_34_68 = c_1257 * c_34 * c_68 
        c_1258_34_67 = c_1258 * c_34 * c_67 
        c_1267_3458 = c_1267 * c_3458 
        c_1268_3457 = c_1268 * c_3457 
        c_1278_3456 = c_1278 * c_3456 
        c_12_345678 = c_12 * c_345678 
        c_12_3456_78 = c_12 * c_3456 * c_78 
        c_12_3457_68 = c_12 * c_3457 * c_68 
        c_12_3458_67 = c_12 * c_3458 * c_67 
        c_1267_34_58 = c_1267 * c_34 * c_58 
        c_1268_34_57 = c_1268 * c_34 * c_57 
        c_12_3467_58 = c_12 * c_3467 * c_58 
        c_12_3468_57 = c_12 * c_3468 * c_57 
        c_1278_34_56 = c_1278 * c_34 * c_56 
        c_12_3478_56 = c_12 * c_3478 * c_56 
        c_12_34_5678 = c_12 * c_34 * c_5678 
        c_12_34_56_78 = c_12 * c_34 * c_56 * c_78 
        c_12_34_57_68 = c_12 * c_34 * c_57 * c_68 
        c_12_34_58_67 = c_12 * c_34 * c_58 * c_67 
        c_1256_37_48 = c_1256 * c_37 * c_48 
        c_1256_38_47 = c_1256 * c_38 * c_47 
        c_1257_36_48 = c_1257 * c_36 * c_48 
        c_1258_36_47 = c_1258 * c_36 * c_47 
        c_1257_38_46 = c_1257 * c_38 * c_46 
        c_1258_37_46 = c_1258 * c_37 * c_46 
        c_1267_35_48 = c_1267 * c_35 * c_48 
        c_1268_35_47 = c_1268 * c_35 * c_47 
        c_12_3567_48 = c_12 * c_3567 * c_48 
        c_12_3568_47 = c_12 * c_3568 * c_47 
        c_1278_35_46 = c_1278 * c_35 * c_46 
        c_12_3578_46 = c_12 * c_3578 * c_46 
        c_12_35_4678 = c_12 * c_35 * c_4678 
        c_12_35_46_78 = c_12 * c_35 * c_46 * c_78 
        c_12_35_47_68 = c_12 * c_35 * c_47 * c_68 
        c_12_35_48_67 = c_12 * c_35 * c_48 * c_67 
        c_1267_38_45 = c_1267 * c_38 * c_45 
        c_1268_37_45 = c_1268 * c_37 * c_45 
        c_1278_36_45 = c_1278 * c_36 * c_45 
        c_12_3678_45 = c_12 * c_3678 * c_45 
        c_12_36_4578 = c_12 * c_36 * c_4578 
        c_12_36_45_78 = c_12 * c_36 * c_45 * c_78 
        c_12_37_4568 = c_12 * c_37 * c_4568 
        c_12_38_4567 = c_12 * c_38 * c_4567 
        c_12_37_45_68 = c_12 * c_37 * c_45 * c_68 
        c_12_38_45_67 = c_12 * c_38 * c_45 * c_67 
        c_12_36_47_58 = c_12 * c_36 * c_47 * c_58 
        c_12_36_48_57 = c_12 * c_36 * c_48 * c_57 
        c_12_37_46_58 = c_12 * c_37 * c_46 * c_58 
        c_12_38_46_57 = c_12 * c_38 * c_46 * c_57 
        c_12_37_48_56 = c_12 * c_37 * c_48 * c_56 
        c_12_38_47_56 = c_12 * c_38 * c_47 * c_56 
        c_134567_28 = c_134567 * c_28 
        c_134568_27 = c_134568 * c_27 
        c_134578_26 = c_134578 * c_26 
        c_1345_2678 = c_1345 * c_2678 
        c_1345_26_78 = c_1345 * c_26 * c_78 
        c_1345_27_68 = c_1345 * c_27 * c_68 
        c_1345_28_67 = c_1345 * c_28 * c_67 
        c_134678_25 = c_134678 * c_25 
        c_1346_2578 = c_1346 * c_2578 
        c_1346_25_78 = c_1346 * c_25 * c_78 
        c_1347_2568 = c_1347 * c_2568 
        c_1348_2567 = c_1348 * c_2567 
        c_1347_25_68 = c_1347 * c_25 * c_68 
        c_1348_25_67 = c_1348 * c_25 * c_67 
        c_1346_27_58 = c_1346 * c_27 * c_58 
        c_1346_28_57 = c_1346 * c_28 * c_57 
        c_1347_26_58 = c_1347 * c_26 * c_58 
        c_1348_26_57 = c_1348 * c_26 * c_57 
        c_1347_28_56 = c_1347 * c_28 * c_56 
        c_1348_27_56 = c_1348 * c_27 * c_56 
        c_135678_24 = c_135678 * c_24 
        c_1356_2478 = c_1356 * c_2478 
        c_1356_24_78 = c_1356 * c_24 * c_78 
        c_1357_2468 = c_1357 * c_2468 
        c_1358_2467 = c_1358 * c_2467 
        c_1357_24_68 = c_1357 * c_24 * c_68 
        c_1358_24_67 = c_1358 * c_24 * c_67 
        c_1367_2458 = c_1367 * c_2458 
        c_1368_2457 = c_1368 * c_2457 
        c_1378_2456 = c_1378 * c_2456 
        c_13_245678 = c_13 * c_245678 
        c_13_2456_78 = c_13 * c_2456 * c_78 
        c_13_2457_68 = c_13 * c_2457 * c_68 
        c_13_2458_67 = c_13 * c_2458 * c_67 
        c_1367_24_58 = c_1367 * c_24 * c_58 
        c_1368_24_57 = c_1368 * c_24 * c_57 
        c_13_2467_58 = c_13 * c_2467 * c_58 
        c_13_2468_57 = c_13 * c_2468 * c_57 
        c_1378_24_56 = c_1378 * c_24 * c_56 
        c_13_2478_56 = c_13 * c_2478 * c_56 
        c_13_24_5678 = c_13 * c_24 * c_5678 
        c_13_24_56_78 = c_13 * c_24 * c_56 * c_78 
        c_13_24_57_68 = c_13 * c_24 * c_57 * c_68 
        c_13_24_58_67 = c_13 * c_24 * c_58 * c_67 
        c_1356_27_48 = c_1356 * c_27 * c_48 
        c_1356_28_47 = c_1356 * c_28 * c_47 
        c_1357_26_48 = c_1357 * c_26 * c_48 
        c_1358_26_47 = c_1358 * c_26 * c_47 
        c_1357_28_46 = c_1357 * c_28 * c_46 
        c_1358_27_46 = c_1358 * c_27 * c_46 
        c_1367_25_48 = c_1367 * c_25 * c_48 
        c_1368_25_47 = c_1368 * c_25 * c_47 
        c_13_2567_48 = c_13 * c_2567 * c_48 
        c_13_2568_47 = c_13 * c_2568 * c_47 
        c_1378_25_46 = c_1378 * c_25 * c_46 
        c_13_2578_46 = c_13 * c_2578 * c_46 
        c_13_25_4678 = c_13 * c_25 * c_4678 
        c_13_25_46_78 = c_13 * c_25 * c_46 * c_78 
        c_13_25_47_68 = c_13 * c_25 * c_47 * c_68 
        c_13_25_48_67 = c_13 * c_25 * c_48 * c_67 
        c_1367_28_45 = c_1367 * c_28 * c_45 
        c_1368_27_45 = c_1368 * c_27 * c_45 
        c_1378_26_45 = c_1378 * c_26 * c_45 
        c_13_2678_45 = c_13 * c_2678 * c_45 
        c_13_26_4578 = c_13 * c_26 * c_4578 
        c_13_26_45_78 = c_13 * c_26 * c_45 * c_78 
        c_13_27_4568 = c_13 * c_27 * c_4568 
        c_13_28_4567 = c_13 * c_28 * c_4567 
        c_13_27_45_68 = c_13 * c_27 * c_45 * c_68 
        c_13_28_45_67 = c_13 * c_28 * c_45 * c_67 
        c_13_26_47_58 = c_13 * c_26 * c_47 * c_58 
        c_13_26_48_57 = c_13 * c_26 * c_48 * c_57 
        c_13_27_46_58 = c_13 * c_27 * c_46 * c_58 
        c_13_28_46_57 = c_13 * c_28 * c_46 * c_57 
        c_13_27_48_56 = c_13 * c_27 * c_48 * c_56 
        c_13_28_47_56 = c_13 * c_28 * c_47 * c_56 
        c_145678_23 = c_145678 * c_23 
        c_1456_2378 = c_1456 * c_2378 
        c_1456_23_78 = c_1456 * c_23 * c_78 
        c_1457_2368 = c_1457 * c_2368 
        c_1458_2367 = c_1458 * c_2367 
        c_1457_23_68 = c_1457 * c_23 * c_68 
        c_1458_23_67 = c_1458 * c_23 * c_67 
        c_1467_2358 = c_1467 * c_2358 
        c_1468_2357 = c_1468 * c_2357 
        c_1478_2356 = c_1478 * c_2356 
        c_14_235678 = c_14 * c_235678 
        c_14_2356_78 = c_14 * c_2356 * c_78 
        c_14_2357_68 = c_14 * c_2357 * c_68 
        c_14_2358_67 = c_14 * c_2358 * c_67 
        c_1467_23_58 = c_1467 * c_23 * c_58 
        c_1468_23_57 = c_1468 * c_23 * c_57 
        c_14_2367_58 = c_14 * c_2367 * c_58 
        c_14_2368_57 = c_14 * c_2368 * c_57 
        c_1478_23_56 = c_1478 * c_23 * c_56 
        c_14_2378_56 = c_14 * c_2378 * c_56 
        c_14_23_5678 = c_14 * c_23 * c_5678 
        c_14_23_56_78 = c_14 * c_23 * c_56 * c_78 
        c_14_23_57_68 = c_14 * c_23 * c_57 * c_68 
        c_14_23_58_67 = c_14 * c_23 * c_58 * c_67 
        c_1567_2348 = c_1567 * c_2348 
        c_1568_2347 = c_1568 * c_2347 
        c_1578_2346 = c_1578 * c_2346 
        c_15_234678 = c_15 * c_234678 
        c_15_2346_78 = c_15 * c_2346 * c_78 
        c_15_2347_68 = c_15 * c_2347 * c_68 
        c_15_2348_67 = c_15 * c_2348 * c_67 
        c_1678_2345 = c_1678 * c_2345 
        c_16_234578 = c_16 * c_234578 
        c_16_2345_78 = c_16 * c_2345 * c_78 
        c_17_234568 = c_17 * c_234568 
        c_18_234567 = c_18 * c_234567 
        c_17_2345_68 = c_17 * c_2345 * c_68 
        c_18_2345_67 = c_18 * c_2345 * c_67 
        c_16_2347_58 = c_16 * c_2347 * c_58 
        c_16_2348_57 = c_16 * c_2348 * c_57 
        c_17_2346_58 = c_17 * c_2346 * c_58 
        c_18_2346_57 = c_18 * c_2346 * c_57 
        c_17_2348_56 = c_17 * c_2348 * c_56 
        c_18_2347_56 = c_18 * c_2347 * c_56 
        c_1567_23_48 = c_1567 * c_23 * c_48 
        c_1568_23_47 = c_1568 * c_23 * c_47 
        c_15_2367_48 = c_15 * c_2367 * c_48 
        c_15_2368_47 = c_15 * c_2368 * c_47 
        c_1578_23_46 = c_1578 * c_23 * c_46 
        c_15_2378_46 = c_15 * c_2378 * c_46 
        c_15_23_4678 = c_15 * c_23 * c_4678 
        c_15_23_46_78 = c_15 * c_23 * c_46 * c_78 
        c_15_23_47_68 = c_15 * c_23 * c_47 * c_68 
        c_15_23_48_67 = c_15 * c_23 * c_48 * c_67 
        c_16_2357_48 = c_16 * c_2357 * c_48 
        c_16_2358_47 = c_16 * c_2358 * c_47 
        c_17_2356_48 = c_17 * c_2356 * c_48 
        c_18_2356_47 = c_18 * c_2356 * c_47 
        c_17_2358_46 = c_17 * c_2358 * c_46 
        c_18_2357_46 = c_18 * c_2357 * c_46 
        c_1678_23_45 = c_1678 * c_23 * c_45 
        c_16_2378_45 = c_16 * c_2378 * c_45 
        c_16_23_4578 = c_16 * c_23 * c_4578 
        c_16_23_45_78 = c_16 * c_23 * c_45 * c_78 
        c_17_2368_45 = c_17 * c_2368 * c_45 
        c_18_2367_45 = c_18 * c_2367 * c_45 
        c_17_23_4568 = c_17 * c_23 * c_4568 
        c_18_23_4567 = c_18 * c_23 * c_4567 
        c_17_23_45_68 = c_17 * c_23 * c_45 * c_68 
        c_18_23_45_67 = c_18 * c_23 * c_45 * c_67 
        c_16_23_47_58 = c_16 * c_23 * c_47 * c_58 
        c_16_23_48_57 = c_16 * c_23 * c_48 * c_57 
        c_17_23_46_58 = c_17 * c_23 * c_46 * c_58 
        c_18_23_46_57 = c_18 * c_23 * c_46 * c_57 
        c_17_23_48_56 = c_17 * c_23 * c_48 * c_56 
        c_18_23_47_56 = c_18 * c_23 * c_47 * c_56 
        c_1456_27_38 = c_1456 * c_27 * c_38 
        c_1456_28_37 = c_1456 * c_28 * c_37 
        c_1457_26_38 = c_1457 * c_26 * c_38 
        c_1458_26_37 = c_1458 * c_26 * c_37 
        c_1457_28_36 = c_1457 * c_28 * c_36 
        c_1458_27_36 = c_1458 * c_27 * c_36 
        c_1467_25_38 = c_1467 * c_25 * c_38 
        c_1468_25_37 = c_1468 * c_25 * c_37 
        c_14_2567_38 = c_14 * c_2567 * c_38 
        c_14_2568_37 = c_14 * c_2568 * c_37 
        c_1478_25_36 = c_1478 * c_25 * c_36 
        c_14_2578_36 = c_14 * c_2578 * c_36 
        c_14_25_3678 = c_14 * c_25 * c_3678 
        c_14_25_36_78 = c_14 * c_25 * c_36 * c_78 
        c_14_25_37_68 = c_14 * c_25 * c_37 * c_68 
        c_14_25_38_67 = c_14 * c_25 * c_38 * c_67 
        c_1467_28_35 = c_1467 * c_28 * c_35 
        c_1468_27_35 = c_1468 * c_27 * c_35 
        c_1478_26_35 = c_1478 * c_26 * c_35 
        c_14_2678_35 = c_14 * c_2678 * c_35 
        c_14_26_3578 = c_14 * c_26 * c_3578 
        c_14_26_35_78 = c_14 * c_26 * c_35 * c_78 
        c_14_27_3568 = c_14 * c_27 * c_3568 
        c_14_28_3567 = c_14 * c_28 * c_3567 
        c_14_27_35_68 = c_14 * c_27 * c_35 * c_68 
        c_14_28_35_67 = c_14 * c_28 * c_35 * c_67 
        c_14_26_37_58 = c_14 * c_26 * c_37 * c_58 
        c_14_26_38_57 = c_14 * c_26 * c_38 * c_57 
        c_14_27_36_58 = c_14 * c_27 * c_36 * c_58 
        c_14_28_36_57 = c_14 * c_28 * c_36 * c_57 
        c_14_27_38_56 = c_14 * c_27 * c_38 * c_56 
        c_14_28_37_56 = c_14 * c_28 * c_37 * c_56 
        c_1567_24_38 = c_1567 * c_24 * c_38 
        c_1568_24_37 = c_1568 * c_24 * c_37 
        c_15_2467_38 = c_15 * c_2467 * c_38 
        c_15_2468_37 = c_15 * c_2468 * c_37 
        c_1578_24_36 = c_1578 * c_24 * c_36 
        c_15_2478_36 = c_15 * c_2478 * c_36 
        c_15_24_3678 = c_15 * c_24 * c_3678 
        c_15_24_36_78 = c_15 * c_24 * c_36 * c_78 
        c_15_24_37_68 = c_15 * c_24 * c_37 * c_68 
        c_15_24_38_67 = c_15 * c_24 * c_38 * c_67 
        c_16_2457_38 = c_16 * c_2457 * c_38 
        c_16_2458_37 = c_16 * c_2458 * c_37 
        c_17_2456_38 = c_17 * c_2456 * c_38 
        c_18_2456_37 = c_18 * c_2456 * c_37 
        c_17_2458_36 = c_17 * c_2458 * c_36 
        c_18_2457_36 = c_18 * c_2457 * c_36 
        c_1678_24_35 = c_1678 * c_24 * c_35 
        c_16_2478_35 = c_16 * c_2478 * c_35 
        c_16_24_3578 = c_16 * c_24 * c_3578 
        c_16_24_35_78 = c_16 * c_24 * c_35 * c_78 
        c_17_2468_35 = c_17 * c_2468 * c_35 
        c_18_2467_35 = c_18 * c_2467 * c_35 
        c_17_24_3568 = c_17 * c_24 * c_3568 
        c_18_24_3567 = c_18 * c_24 * c_3567 
        c_17_24_35_68 = c_17 * c_24 * c_35 * c_68 
        c_18_24_35_67 = c_18 * c_24 * c_35 * c_67 
        c_16_24_37_58 = c_16 * c_24 * c_37 * c_58 
        c_16_24_38_57 = c_16 * c_24 * c_38 * c_57 
        c_17_24_36_58 = c_17 * c_24 * c_36 * c_58 
        c_18_24_36_57 = c_18 * c_24 * c_36 * c_57 
        c_17_24_38_56 = c_17 * c_24 * c_38 * c_56 
        c_18_24_37_56 = c_18 * c_24 * c_37 * c_56 
        c_1567_28_34 = c_1567 * c_28 * c_34 
        c_1568_27_34 = c_1568 * c_27 * c_34 
        c_1578_26_34 = c_1578 * c_26 * c_34 
        c_15_2678_34 = c_15 * c_2678 * c_34 
        c_15_26_3478 = c_15 * c_26 * c_3478 
        c_15_26_34_78 = c_15 * c_26 * c_34 * c_78 
        c_15_27_3468 = c_15 * c_27 * c_3468 
        c_15_28_3467 = c_15 * c_28 * c_3467 
        c_15_27_34_68 = c_15 * c_27 * c_34 * c_68 
        c_15_28_34_67 = c_15 * c_28 * c_34 * c_67 
        c_1678_25_34 = c_1678 * c_25 * c_34 
        c_16_2578_34 = c_16 * c_2578 * c_34 
        c_16_25_3478 = c_16 * c_25 * c_3478 
        c_16_25_34_78 = c_16 * c_25 * c_34 * c_78 
        c_17_2568_34 = c_17 * c_2568 * c_34 
        c_18_2567_34 = c_18 * c_2567 * c_34 
        c_17_25_3468 = c_17 * c_25 * c_3468 
        c_18_25_3467 = c_18 * c_25 * c_3467 
        c_17_25_34_68 = c_17 * c_25 * c_34 * c_68 
        c_18_25_34_67 = c_18 * c_25 * c_34 * c_67 
        c_16_27_3458 = c_16 * c_27 * c_3458 
        c_16_28_3457 = c_16 * c_28 * c_3457 
        c_17_26_3458 = c_17 * c_26 * c_3458 
        c_18_26_3457 = c_18 * c_26 * c_3457 
        c_17_28_3456 = c_17 * c_28 * c_3456 
        c_18_27_3456 = c_18 * c_27 * c_3456 
        c_16_27_34_58 = c_16 * c_27 * c_34 * c_58 
        c_16_28_34_57 = c_16 * c_28 * c_34 * c_57 
        c_17_26_34_58 = c_17 * c_26 * c_34 * c_58 
        c_18_26_34_57 = c_18 * c_26 * c_34 * c_57 
        c_17_28_34_56 = c_17 * c_28 * c_34 * c_56 
        c_18_27_34_56 = c_18 * c_27 * c_34 * c_56 
        c_15_26_37_48 = c_15 * c_26 * c_37 * c_48 
        c_15_26_38_47 = c_15 * c_26 * c_38 * c_47 
        c_15_27_36_48 = c_15 * c_27 * c_36 * c_48 
        c_15_28_36_47 = c_15 * c_28 * c_36 * c_47 
        c_15_27_38_46 = c_15 * c_27 * c_38 * c_46 
        c_15_28_37_46 = c_15 * c_28 * c_37 * c_46 
        c_16_25_37_48 = c_16 * c_25 * c_37 * c_48 
        c_16_25_38_47 = c_16 * c_25 * c_38 * c_47 
        c_17_25_36_48 = c_17 * c_25 * c_36 * c_48 
        c_18_25_36_47 = c_18 * c_25 * c_36 * c_47 
        c_17_25_38_46 = c_17 * c_25 * c_38 * c_46 
        c_18_25_37_46 = c_18 * c_25 * c_37 * c_46 
        c_16_27_35_48 = c_16 * c_27 * c_35 * c_48 
        c_16_28_35_47 = c_16 * c_28 * c_35 * c_47 
        c_17_26_35_48 = c_17 * c_26 * c_35 * c_48 
        c_18_26_35_47 = c_18 * c_26 * c_35 * c_47 
        c_17_28_35_46 = c_17 * c_28 * c_35 * c_46 
        c_18_27_35_46 = c_18 * c_27 * c_35 * c_46 
        c_16_27_38_45 = c_16 * c_27 * c_38 * c_45 
        c_16_28_37_45 = c_16 * c_28 * c_37 * c_45 
        c_17_26_38_45 = c_17 * c_26 * c_38 * c_45 
        c_18_26_37_45 = c_18 * c_26 * c_37 * c_45 
        c_17_28_36_45 = c_17 * c_28 * c_36 * c_45 
        c_18_27_36_45 = c_18 * c_27 * c_36 * c_45 


        y =  st.mean([a * b * c * d * e * f* g* h for a,b,c,d,e,f,g,h in zip(r1,r2,r3,r4,r5,r6,r7,r8)]) - (c_18_234567 +
        c_17_234568 +    
        c_1678_2345 +    
        c_16_234578 +    
        c_1578_2346 +    
        c_1568_2347 +    
        c_1567_2348 +    
        c_15_234678 +    
        c_1478_2356 +    
        c_1468_2357 +    
        c_1467_2358 +    
        c_1458_2367 +    
        c_1457_2368 +    
        c_145678_23 +    
        c_1456_2378 +    
        c_14_235678 +    
        c_1378_2456 +    
        c_1368_2457 +    
        c_1367_2458 +    
        c_1358_2467 +    
        c_1357_2468 +    
        c_135678_24 +    
        c_1356_2478 +    
        c_1348_2567 +    
        c_1347_2568 +    
        c_134678_25 +    
        c_1346_2578 +    
        c_134578_26 +    
        c_134568_27 +    
        c_134567_28 +    
        c_1345_2678 +    
        c_13_245678 +    
        c_1278_3456 +    
        c_1268_3457 +    
        c_1267_3458 +    
        c_1258_3467 +    
        c_1257_3468 +    
        c_125678_34 +    
        c_1256_3478 +    
        c_1248_3567 +    
        c_1247_3568 +    
        c_124678_35 +    
        c_1246_3578 +    
        c_124578_36 +    
        c_124568_37 +    
        c_124567_38 +    
        c_1245_3678 +    
        c_1238_4567 +    
        c_1237_4568 +    
        c_123678_45 +    
        c_1236_4578 +    
        c_123578_46 +    
        c_123568_47 +    
        c_123567_48 +    
        c_1235_4678 +    
        c_123478_56 +    
        c_123468_57 +    
        c_123467_58 +    
        c_123458_67 +    
        c_123457_68 +    
        c_12_345678 +    
        c_1234_5678 +    
        c_123456_78 +    
          
        c_18_27_3456 +    
        c_18_26_3457 +    
        c_18_2567_34 +    
        c_18_25_3467 +    
        c_18_2467_35 +    
        c_18_2457_36 +    
        c_18_2456_37 +    
        c_18_24_3567 +    
        c_18_2367_45 +    
        c_18_2357_46 +    
        c_18_2356_47 +    
        c_18_2347_56 +    
        c_18_2346_57 +    
        c_18_23_4567 +    
        c_18_2345_67 +    
        c_17_28_3456 +    
        c_17_26_3458 +    
        c_17_2568_34 +    
        c_17_25_3468 +    
        c_17_2468_35 +    
        c_17_2458_36 +    
        c_17_2456_38 +    
        c_17_24_3568 +    
        c_17_2368_45 +    
        c_17_2358_46 +    
        c_17_2356_48 +    
        c_17_2348_56 +    
        c_17_2346_58 +    
        c_17_23_4568 +    
        c_17_2345_68 +    
        c_1678_25_34 +    
        c_1678_24_35 +    
        c_1678_23_45 +    
        c_16_28_3457 +    
        c_16_27_3458 +    
        c_16_2578_34 +    
        c_16_25_3478 +    
        c_16_2478_35 +    
        c_16_2458_37 +    
        c_16_2457_38 +    
        c_16_24_3578 +    
        c_16_2378_45 +    
        c_16_2358_47 +    
        c_16_2357_48 +    
        c_16_2348_57 +    
        c_16_2347_58 +    
        c_16_23_4578 +    
        c_16_2345_78 +    
        c_1578_26_34 +    
        c_1578_24_36 +    
        c_1578_23_46 +    
        c_1568_27_34 +    
        c_1568_24_37 +    
        c_1568_23_47 +    
        c_1567_28_34 +    
        c_1567_24_38 +    
        c_1567_23_48 +    
        c_15_28_3467 +    
        c_15_27_3468 +    
        c_15_2678_34 +    
        c_15_26_3478 +    
        c_15_2478_36 +    
        c_15_2468_37 +    
        c_15_2467_38 +    
        c_15_24_3678 +    
        c_15_2378_46 +    
        c_15_2368_47 +    
        c_15_2367_48 +    
        c_15_2348_67 +    
        c_15_2347_68 +    
        c_15_23_4678 +    
        c_15_2346_78 +    
        c_1478_26_35 +    
        c_1478_25_36 +    
        c_1478_23_56 +    
        c_1468_27_35 +    
        c_1468_25_37 +    
        c_1468_23_57 +    
        c_1467_28_35 +    
        c_1467_25_38 +    
        c_1467_23_58 +    
        c_1458_27_36 +    
        c_1458_26_37 +    
        c_1458_23_67 +    
        c_1457_28_36 +    
        c_1457_26_38 +    
        c_1457_23_68 +    
        c_1456_28_37 +    
        c_1456_27_38 +    
        c_1456_23_78 +    
        c_14_28_3567 +    
        c_14_27_3568 +    
        c_14_2678_35 +    
        c_14_26_3578 +    
        c_14_2578_36 +    
        c_14_2568_37 +    
        c_14_2567_38 +    
        c_14_25_3678 +    
        c_14_2378_56 +    
        c_14_2368_57 +    
        c_14_2367_58 +    
        c_14_2358_67 +    
        c_14_2357_68 +    
        c_14_23_5678 +    
        c_14_2356_78 +    
        c_1378_26_45 +    
        c_1378_25_46 +    
        c_1378_24_56 +    
        c_1368_27_45 +    
        c_1368_25_47 +    
        c_1368_24_57 +    
        c_1367_28_45 +    
        c_1367_25_48 +    
        c_1367_24_58 +    
        c_1358_27_46 +    
        c_1358_26_47 +    
        c_1358_24_67 +    
        c_1357_28_46 +    
        c_1357_26_48 +    
        c_1357_24_68 +    
        c_1356_28_47 +    
        c_1356_27_48 +    
        c_1356_24_78 +    
        c_1348_27_56 +    
        c_1348_26_57 +    
        c_1348_25_67 +    
        c_1347_28_56 +    
        c_1347_26_58 +    
        c_1347_25_68 +    
        c_1346_28_57 +    
        c_1346_27_58 +    
        c_1346_25_78 +    
        c_1345_28_67 +    
        c_1345_27_68 +    
        c_1345_26_78 +    
        c_13_28_4567 +    
        c_13_27_4568 +    
        c_13_2678_45 +    
        c_13_26_4578 +    
        c_13_2578_46 +    
        c_13_2568_47 +    
        c_13_2567_48 +    
        c_13_25_4678 +    
        c_13_2478_56 +    
        c_13_2468_57 +    
        c_13_2467_58 +    
        c_13_2458_67 +    
        c_13_2457_68 +    
        c_13_24_5678 +    
        c_13_2456_78 +    
        c_1278_36_45 +    
        c_1278_35_46 +    
        c_1278_34_56 +    
        c_1268_37_45 +    
        c_1268_35_47 +    
        c_1268_34_57 +    
        c_1267_38_45 +    
        c_1267_35_48 +    
        c_1267_34_58 +    
        c_1258_37_46 +    
        c_1258_36_47 +    
        c_1258_34_67 +    
        c_1257_38_46 +    
        c_1257_36_48 +    
        c_1257_34_68 +    
        c_1256_38_47 +    
        c_1256_37_48 +    
        c_1256_34_78 +    
        c_1248_37_56 +    
        c_1248_36_57 +    
        c_1248_35_67 +    
        c_1247_38_56 +    
        c_1247_36_58 +    
        c_1247_35_68 +    
        c_1246_38_57 +    
        c_1246_37_58 +    
        c_1246_35_78 +    
        c_1245_38_67 +    
        c_1245_37_68 +    
        c_1245_36_78 +    
        c_1238_47_56 +    
        c_1238_46_57 +    
        c_12_38_4567 +    
        c_1238_45_67 +    
        c_1237_48_56 +    
        c_1237_46_58 +    
        c_12_37_4568 +    
        c_1237_45_68 +    
        c_12_3678_45 +    
        c_1236_48_57 +    
        c_1236_47_58 +    
        c_12_36_4578 +    
        c_1236_45_78 +    
        c_12_3578_46 +    
        c_12_3568_47 +    
        c_12_3567_48 +    
        c_1235_48_67 +    
        c_1235_47_68 +    
        c_12_35_4678 +    
        c_1235_46_78 +    
        c_12_3478_56 +    
        c_12_3468_57 +    
        c_12_3467_58 +    
        c_12_3458_67 +    
        c_1234_58_67 +    
        c_12_3457_68 +    
        c_1234_57_68 +    
        c_12_34_5678 +    
        c_12_3456_78 +    
        c_1234_56_78 +    
          
        c_18_27_36_45 +    
        c_18_27_35_46 +    
        c_18_27_34_56 +    
        c_18_26_37_45 +    
        c_18_26_35_47 +    
        c_18_26_34_57 +    
        c_18_25_37_46 +    
        c_18_25_36_47 +    
        c_18_25_34_67 +    
        c_18_24_37_56 +    
        c_18_24_36_57 +    
        c_18_24_35_67 +    
        c_18_23_47_56 +    
        c_18_23_46_57 +    
        c_18_23_45_67 +    
        c_17_28_36_45 +    
        c_17_28_35_46 +    
        c_17_28_34_56 +    
        c_17_26_38_45 +    
        c_17_26_35_48 +    
        c_17_26_34_58 +    
        c_17_25_38_46 +    
        c_17_25_36_48 +    
        c_17_25_34_68 +    
        c_17_24_38_56 +    
        c_17_24_36_58 +    
        c_17_24_35_68 +    
        c_17_23_48_56 +    
        c_17_23_46_58 +    
        c_17_23_45_68 +    
        c_16_28_37_45 +    
        c_16_28_35_47 +    
        c_16_28_34_57 +    
        c_16_27_38_45 +    
        c_16_27_35_48 +    
        c_16_27_34_58 +    
        c_16_25_38_47 +    
        c_16_25_37_48 +    
        c_16_25_34_78 +    
        c_16_24_38_57 +    
        c_16_24_37_58 +    
        c_16_24_35_78 +    
        c_16_23_48_57 +    
        c_16_23_47_58 +    
        c_16_23_45_78 +    
        c_15_28_37_46 +    
        c_15_28_36_47 +    
        c_15_28_34_67 +    
        c_15_27_38_46 +    
        c_15_27_36_48 +    
        c_15_27_34_68 +    
        c_15_26_38_47 +    
        c_15_26_37_48 +    
        c_15_26_34_78 +    
        c_15_24_38_67 +    
        c_15_24_37_68 +    
        c_15_24_36_78 +    
        c_15_23_48_67 +    
        c_15_23_47_68 +    
        c_15_23_46_78 +    
        c_14_28_37_56 +    
        c_14_28_36_57 +    
        c_14_28_35_67 +    
        c_14_27_38_56 +    
        c_14_27_36_58 +    
        c_14_27_35_68 +    
        c_14_26_38_57 +    
        c_14_26_37_58 +    
        c_14_26_35_78 +    
        c_14_25_38_67 +    
        c_14_25_37_68 +    
        c_14_25_36_78 +    
        c_14_23_58_67 +    
        c_14_23_57_68 +    
        c_14_23_56_78 +    
        c_13_28_47_56 +    
        c_13_28_46_57 +    
        c_13_28_45_67 +    
        c_13_27_48_56 +    
        c_13_27_46_58 +    
        c_13_27_45_68 +    
        c_13_26_48_57 +    
        c_13_26_47_58 +    
        c_13_26_45_78 +    
        c_13_25_48_67 +    
        c_13_25_47_68 +    
        c_13_25_46_78 +    
        c_13_24_58_67 +    
        c_13_24_57_68 +    
        c_13_24_56_78 +    
        c_12_38_47_56 +    
        c_12_38_46_57 +    
        c_12_38_45_67 +    
        c_12_37_48_56 +    
        c_12_37_46_58 +    
        c_12_37_45_68 +    
        c_12_36_48_57 +    
        c_12_36_47_58 +    
        c_12_36_45_78 +    
        c_12_35_48_67 +    
        c_12_35_47_68 +    
        c_12_35_46_78 +    
        c_12_34_58_67 +    
        c_12_34_57_68 +    
        c_12_34_56_78) 

        return y

