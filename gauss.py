# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 18:24:45 2014

FEHLERFORMELN V355
@author: martin
"""

from sympy import var, pi, sqrt

def error(f, err_vars=None):
    from sympy import Symbol, latex
    s = 0
    latex_names = dict()
    
    if err_vars == None:
        err_vars = f.free_symbols
        
    for v in err_vars:
        err = Symbol('latex_std_' + v.name)
        s += f.diff(v)**2 * err**2
        latex_names[err] = '\\sigma_{' + latex(v) + '}'
        
    return latex(sqrt(s), symbol_names=latex_names)



L,C_K, C = var('L C_K C')

nu_p = 1/(2*pi*sqrt(L*C))
nu_m = 1/(2*pi*sqrt(L*(1/C+2/C_K)-1))
print(error(nu_p))
print('------')
print(error(nu_m))