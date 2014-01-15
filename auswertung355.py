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

"###########################################################"

"AUFGABENTEIL A"
"aCk=Werte von Ck in Teil a, Cka=Werte in korrekter Größenordnung für Teil a"
"bcCk=Werte von Ck in Teil b und c, Ck=in korrekter Größenordnung"
"aVerhaeltnis: Verhältnis von kleiner zu großer Welle"
"Experimentelle Werte:"
aCk=array([ufloat(2.03,0.0609),ufloat(3.00,0.09),ufloat(4.00,0.12),ufloat(5.02,0.1506),ufloat(6.47,0.1941),ufloat(8.00,0.24),ufloat(9.99,0.2997)])
aVerhaeltnis=array([ufloat(3.5,0.5),ufloat(4.5,0.5),ufloat(6.5,0.5),ufloat(8,0.5),ufloat(9.75,0.5),ufloat(11,0.5),ufloat(13,0.5)])
Cka = aCk / 1000000000
bcCk=array([ufloat(1.01,0.0303),ufloat(2.03,0.0609),ufloat(3.00,0.09),ufloat(4.00,0.12),ufloat(5.02,0.1506),ufloat(6.47,0.1941),ufloat(8.00,0.24),ufloat(9.99,0.2997)])
Ck=bcCk/1000000000
"Theoretische Werte berechnen:"
L = ufloat(0.032351, 0.00005)

C = ufloat(0.0000000008051, 0.0000000000005)

Csp = 0.000000000037

print "Aufgabenteil A:"
print "nuePlus:"
nuePlus = 1/(2*math.pi*(L*(C+Csp))**(0.5))
print nuePlus

print "nueMinus:"
nueMinus=1/(2*math.pi*(L*((1/C)+(2/Cka))**(-1)+L*Csp)**0.5)
print nueMinus

"nueMittel ist der Mittelwert der beiden Nüs"
print "nueMittel:"
nueMittel = (0.5*(nuePlus+nueMinus))
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

tab1 = array([Cka,aVerhaeltnis,nueMinus,nueMittel,schwebung,verhaeltnis,abweichungen])
print make_LaTeX_table(tab1.T, [r'Ck',r'verhaeltnis',r'nieMinustheo',r'nueMittel',r'schwebung',r'verhältnis',r'abweichungen'])

"###########################################################"

"AUFGABENTEIL B"
"Theoretisch berechnete Werte:"
print "Aufgabenteil B:"
print "nuePlus"
print nuePlus
print "nueMinus"
print nueMinus
"Experimentell bestimmte Werte:"
"exnuePlus/Minus= gemessene Werte"
exnuePlus=array([30490,30490,30490,30490,30490,30490,30490])
exnueMinus=array([40010,37300,35760,34780,33880,33280,33750])
"Hier kommt der Vergleich mit den Theoriewerten aus a"
abwPlusTeilB=abs(exnuePlus/nuePlus)
abwMinusTeilB=abs(exnueMinus/nueMinus)

data = array([exnueMinus,exnuePlus])
print make_LaTeX_table(data.T, [r'Spalte1',r'test'])
print "Abweichung in Prozent von Nue+"
print abwPlusTeilB
print "Abweichung in Prozent von Nue-"
print abwMinusTeilB

tab2 = array([nueMinus,exnuePlus,exnueMinus,abwPlusTeilB,abwMinusTeilB])
print make_LaTeX_table(tab2.T, [r'nueminus',r'explus',r'exminus',r'abwplus',r'abwminus'])
"###########################################################"

"AUFGABENTEIL C"
"Messwerte:"
time=21
flow=3800
fhigh=74200
peak1time=ufloat(9,0.5)
peak2time=array([ufloat(13.7,0.5),ufloat(11.8,0.5),ufloat(10.9,0.5),ufloat(10.5,0.5),ufloat(10.1,0.5),ufloat(9.9,0.5),ufloat(9.5,0.5),ufloat(9.5,0.5)])

print "Aufgabenteil C:"
"Peakzeiten auf Frequenzen umrechnen:"
peak1freq=(70400*peak1time/21)+3800
peak2freq=(70400*peak2time/21) +3800
print "peak1freq"
print peak1freq
print "peak2freq:"
print peak2freq
peak1=array([ufloat(1.22,0.05),ufloat(1.25,0.05),ufloat(1.25,0.05),ufloat(1.3,0.05),ufloat(1.33,0.05),ufloat(1.4,0.05),ufloat(1.46,0.05),ufloat(1.55,0.05)])
peak2=array([ufloat(0.9,0.05),ufloat(1.02,0.05),ufloat(1.1,0.05),ufloat(1.15,0.05),ufloat(1.19,0.05),ufloat(1.3,0.05),ufloat(1.34,0.05),ufloat(1.43,0.05)])
I1=(peak1/73)
I2=(peak2/73)
print "I1:"
print I1
print "I2:"
print I2


 
Cke = 2.03

def Lbetrag(f):
    return((1/(8*math.pi**2*Cke**2*48**2*(2*math.pi*L-1/(2*math.pi*f)*(1/C + 1/Cke))**2+(1/(2*math.pi*f*Cke)-2*math.pi*f*(2*math.pi*L-1/(2*math.pi*f)*(1/C + 1/Cke))**2+2*math.pi*f*48*22*Cke)**2)**0.5))
  

"###########################################################"


"AUFGABENTEIL VORBEREITUNG UND JUSTIERUNG:"
"Berechnung Vergleich der Resonanzfrequenzen:"
fFein=30700
fTheorie=30492.5990436
vergleich=abs((fFein/fTheorie-1)*100)
print "VORBEREITUNG VERGLEICH:"
print vergleich