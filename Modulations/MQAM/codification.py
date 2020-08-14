from sympy.combinatorics.graycode import GrayCode

class Codification:

    def bin2Dec(bin,ld):
        dec = GrayCode(ld, start=bin).rank
        return dec
