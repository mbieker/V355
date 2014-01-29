# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:44:42 2013
@author: martin + julian
"""
#Using the magic encoding
#-*- coding: utf-8 -*-
from scipy import * 
import matplotlib.pyplot as p


from uncertainties import *
import math


def make_LaTeX_table(data,header, flip= 'false', onedim = 'false'):
    output = '\\begin{table}\n\\centering\n\\begin{tabular}{'
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
        
        for i in range(col_cnt):
            output += 'l'
        output += '}\n\\toprule\n{'+ header[0]
        for i in range (1,col_cnt):
            output += '} &{ ' + header[i]
        output += ' }\\\\\n\\midrule\n'
        for i in data:
            if(isinstance(i[0],(int,float,int32))):
                output +=  str( i[0] ) 
            else:
                output += ' ${:L}$ '.format(i[0])
            for j in range(1,col_cnt):
                if(isinstance(i[j],(int,float,int32))):
                    output += ' & ' + str( i[j])   
                else:          
                    output += ' & ${:L}$ '.format(i[j])                
                
            output += '\\\\\n'
        output += '\\bottomrule\n\\end{tabular}\n\\label{}\n\\caption{}\n\\end{table}\n'
                            
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

nuePlus = 1/(2*math.pi*(L*(C+Csp))**(0.5))


nueMinus=1/(2*math.pi*(L*((1/C)+(2/Cka))**(-1)+L*Csp)**0.5)

nueMittel = (0.5*(nuePlus+nueMinus))
schwebung =abs(nuePlus-nueMinus)



verhaeltnis = nueMittel / schwebung

n = range(1,8)
abweichungen = abs(aVerhaeltnis/verhaeltnis*100-100)


table_1 = array([n,aCk,aVerhaeltnis])
print "############################"
print make_LaTeX_table(table_1.T, ["n",r"$\frac{C_K}{\si{\nano\farad}}$", r"Frequenzverh\"altnis"])
print "###########################################################"
table_2 = array([n,nueMittel,schwebung,verhaeltnis])
table_3 = array([n,aVerhaeltnis,verhaeltnis, abweichungen])

print make_LaTeX_table(table_2.T, ["","","",""])
print "##############"
print make_LaTeX_table(table_3.T, ["","","",""])

"AUFGABENTEIL B"
"Theoretisch berechnete Werte:"
print "Aufgabenteil B:"

"Experimentell bestimmte Werte:"
"exnuePlus/Minus= gemessene Werte"
exnuePlus=array([30490,30490,30490,30490,30490,30490,30490])
exnueMinus=array([40010,37300,35760,34780,33880,33280,33750])
"Hier kommt der Vergleich mit den Theoriewerten aus a"
abwPlusTeilB=abs(exnuePlus/nuePlus)
abwMinusTeilB=abs(exnueMinus/nueMinus)

data = array([exnueMinus,exnuePlus])

tab4 = array([[bcCk[i],nueMinus[i],exnuePlus[i],exnueMinus[i],round(abwPlusTeilB[i].n,3),round(abwMinusTeilB[i].n,3)] for i in range(7)])
print make_LaTeX_table(tab4, [r'nueminus',r'explus',r'exminus',r'abwplus',r'abwminus' , 's'])
"###########################################################"

"AUFGABENTEIL C"
"Messwerte:"
time=21
flow=3800
fhigh=74200
peak1time=array([ufloat(9,0.5),ufloat(9,0.5),ufloat(9,0.5),ufloat(9,0.5),ufloat(9,0.5),ufloat(9,0.5),ufloat(9,0.5),ufloat(9,0.5)])
peak2time=array([ufloat(13.7,0.5),ufloat(11.8,0.5),ufloat(10.9,0.5),ufloat(10.5,0.5),ufloat(10.1,0.5),ufloat(9.9,0.5),ufloat(9.5,0.5),ufloat(9.5,0.5)])

print "Aufgabenteil C:"
"Peakzeiten auf Frequenzen umrechnen:"
peak1freq=(70400*peak1time/21)+3800
peak2freq=(70400*peak2time/21) +3800

peak1=array([ufloat(1.22,0.05),ufloat(1.25,0.05),ufloat(1.25,0.05),ufloat(1.3,0.05),ufloat(1.33,0.05),ufloat(1.4,0.05),ufloat(1.46,0.05),ufloat(1.55,0.05)])
peak2=array([ufloat(0.9,0.05),ufloat(1.02,0.05),ufloat(1.1,0.05),ufloat(1.15,0.05),ufloat(1.19,0.05),ufloat(1.3,0.05),ufloat(1.34,0.05),ufloat(1.43,0.05)])
I1=(peak1/73)
I2=(peak2/73)
Cke = 2.03


tab5 = [bcCk,peak1time,peak2time,peak1,peak2]

header5 = [r"$\frac{C_K}{\si{\nano\farad}}$",r"$\frac{t_1}{\si{\mili\second}}$" ,r"$\frac{t_2}{\si{\mili\second}}$" , r"$\frac{U_1}{\si{\volt}}$" , r"$\frac{U_2}{\si{\volt}}$"] 
def Lbetrag(f):
    return((1/(8*math.pi**2*Cke**2*48**2*(2*math.pi*L-1/(2*math.pi*f)*(1/C + 1/Cke))**2+(1/(2*math.pi*f*Cke)-2*math.pi*f*(2*math.pi*L-1/(2*math.pi*f)*(1/C + 1/Cke))**2+2*math.pi*f*48*22*Cke)**2)**0.5))
  
print "Tabelle 5"

print make_LaTeX_table(array(tab5).T, header5)
"###########################################################"

tab6 = array([bcCk, peak1freq, peak2freq , I1, I2])
header6 =  [r"$\frac{C_K}{\si{\nano\farad}}$",r"$\frac{\nu_1}{\si{\Hz}}$" ,r"$\frac{nu_2}{\si{\Hz}}$" , r"$\frac{I_1}{\si{\ampere}}$" , r"$\frac{I_2}{\si{\ampere}}$"] 


print "Tabelle 6"

print make_LaTeX_table(tab6.T, header6)



# Zu jedem Versuchsteil ein Plot:

# a) verhälntis vs c_k
p.close()
plot_cka = array([i.n for i in aCk])
plot_vhexp = array([i.n for i in aVerhaeltnis])
plot_vhth = array([i.n for i in verhaeltnis])
p.plot(plot_cka,plot_vhexp, 'x', label= 'Messwerte')
p.plot(plot_cka,plot_vhth, 'o', label = 'berechnete Werte')
p.xlabel(r"$C_K$ in nF")
p.ylabel(r"$\frac{\nu_{Schweb.}}{\overline{\nu}}$",rotation =0)
p.legend()
p.subplots_adjust(left=0.2)
p.savefig('Abb/diag1.png')
p.close()

# nu_- vs C_k

plot_ckb = array([ bcCk[i].n for i in  range(8)])

nu_minus_range = array([1/(2*math.pi*(L.n*((1/C.n)+(2/i))**(-1)+L.n*Csp)**0.5) for i in 1e-9*linspace(2,10)])

p.plot(plot_ckb[1:],exnueMinus,'x', label = "Messwerte")
p.plot(linspace(2,10),nu_minus_range, label = "Theoriekurve")
p.xlabel(r"$C_K$ in nF")
p.ylabel(r"$\nu_-$ in Hz",rotation =0)
p.legend()
p.subplots_adjust(left=0.2)
p.savefig('./Abb/diag2.png')
p.close()

nu_plus_range = array([1/(2*math.pi*(L.n*(C.n+Csp))**(0.5)) for i in 1e-9*linspace(2,10)])

p.plot(plot_ckb[1:],exnuePlus,'x', label = "Messwerte")
p.plot(linspace(2,10),nu_plus_range, label = "Theoriekurve")
p.xlabel(r"$C_K$ in nF")
p.ylabel(r"$\nu_+$ in Hz",rotation =0)
p.legend()
p.ylim(30.4e3,30.6e3)
p.subplots_adjust(left=0.2)
p.savefig('./Abb/diag3.png')
p.close()
# I_ vs. C_k


plot_I_1 = array([i.n for i in I1])
plot_I_2 = array([i.n for i in I2])

p.plot(plot_ckb,plot_I_1, 'x', label = "$I_1$")
p.plot(plot_ckb,plot_I_2, 'o', label = "$I_2$")
p.legend()
p.xlim(0,11)
p.xlabel(r"$C_K$ in nF")
p.ylabel(r"$I$ in A",rotation = 0)
p.subplots_adjust(left=0.15)
p.savefig('./Abb/diag4.png')

p.close()