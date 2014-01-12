# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:44:42 2013
@author: martin + julian
"""
#Using the magic encoding
#-*- coding: utf-8 -*-
from scipy import * 
from matplotlib.pyplot import *
import matplotlib as mp
mp.rc('text', usetex=True)
from uncertainties import *
import math


def make_LaTeX_table(data,header, flip= 'false', onedim = 'false'):
    output = '\\begin{tabular}{'
    #Get dimensions
    if(onedim == 'true'):
        if(flip == 'false'):
        
            data = array([[i] for i in data])
        
        else:
            data = array([data])
        

    row_cnt, col_cnt = data.shape
    header_cnt = len(header)
    
    if(header_cnt == col_cnt and flip== 'false'):
        #Make Format
        output += '|'
        for i in range(col_cnt):
            output += 'c|'
        output += '}\n\\hline\n'+ header[0]
        for i in range (1,col_cnt):
            output += ' & ' +  header[i]
        output += ' \\\\\n\\hline\n'
        for i in data:
            output += str(i[0])
            for j in range(1,col_cnt):
                output += ' & ' + str( i[j])
            output += '\\\\\n'
        output += '\\hline\n\\end{tabular}\n'
                            
        return output
    else:
        if(row_cnt == header_cnt):
            output += '|c|' + (col_cnt)*'c' + '|}\n\\hline\n'
            for i in range(row_cnt):
                output += header[i] 
                for j in range(col_cnt):
                    output += ' & ' + str(data[i][j])
                output += '\\\\\n\\hline\n'
                
            output += '\\end{tabular}\n'  
            return output
        else:
            return 'ERROR'

    
def err(data):
    mean = data.mean()
    N = len(data)
    err = 0
    for i in data:
        err += (i - mean)**2
    err = sqrt(err/((N-1)*N))
    return ufloat(mean,err)


def lin_reg(x,y):
    N = len(x)
    sumx = x.sum()
    sumy = y.sum()
    sumxx = (x*x).sum()
    sumxy = (x*y).sum()
    m = (sumxy -  sumx*sumy/N)/(sumxx- sumx**2/N)
    b = sumy/N - m*sumx/N
    
    sy = sqrt(((y - m*x - b)**2).sum()/(N-1))
    m_err = sy *sqrt(N/(N*sumxx - sumx**2))
    b_err= m_err * sqrt(sumxx/N)
    return m,b,m_err,b_err



"AUFGABENTEIL A"
"Experimentelle Werte:"
aCk=array([2.03,3.00,4.00,5.02,6.47,8.00,9.99])
aVerhaeltnis=array([3.5,4.5,6.5,8,9.75,11,13])
Cka = aCk / 1000000000
bcCk=array([2.03,3.00,4.00,5.02,6.47,8.00,9.99])
Ck=bcCk/1000000000
"Theoretische Werte berechnen:"
L = 0.032351 

C = 0.0000000008051

Csp = 0.000000000037

print "Aufgabenteil A:"
print "nuePlus:"
nuePlus = 1/(2*math.pi*(L*(C+Csp))**(0.5))
print nuePlus

print "nueMinus:"
nueMinus=1/(2*math.pi*sqrt(L*((1/C)+(2/Cka))**(-1)+L*Csp))
print nueMinus

print "nueMittel:"
nueMittel=0.5*(nuePlus+nueMinus)
print nueMittel

print "schwebung:"
schwebung = nueMinus - nuePlus
print schwebung

print "verhältnis:"
verhaeltnis = nueMittel / schwebung
print verhaeltnis

print "abweichungen in Prozent:"
abweichungen = abs(aVerhaeltnis/verhaeltnis*100-100)
print abweichungen



"AUFGABENTEIL B"
"Theoretisch berechnete Werte:"
print "Aufgabenteil B:"
print "nuePlus"
print nuePlus
print "nueMinus"
print nueMinus
"Experimentell bestimmte Werte:"
exnuePlus=array([30490,30490,30490,30490,30490,30490,30490])
exnueMinus=array([40010,37300,35760,34780,33880,33280,33750])
abwPlusTeilB=abs(exnuePlus/nuePlus)
abwMinusTeilB=abs(exnueMinus/nueMinus)
print "Abweichung in Prozent von Nue+"
print abwPlusTeilB
print "Abweichung in Prozent von Nue-"
print abwMinusTeilB



"AUFGABENTEIL C"
"Messwerte:"
time=21
flow=3800
fhigh=74200
peak1time=9
peak2time=array([13.7,11.8,10.9,10.5,10.1,9.9,9.5,9.5])
peak1=array([1.22,1.25,1.25,1.3,1.33,1.4,1.46,1.55])
peak2=array([0.9,1.02,1.1,1.15,1.19,1.3,1.34,1.43])

print "Aufgabenteil C:"
"Peakzeiten auf Frequenzen umrechnen:"
peak1freq=(70400*9/21)+3800
peak2freq=(70400*peak2time/21) +3800
print "peak1freq"
print peak1freq
print "peak2freq:"
print peak2freq
