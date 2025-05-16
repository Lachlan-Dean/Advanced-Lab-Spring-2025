import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.umath import *

R_cons = 1.0973731e7
m_h = 1.6735e-27 
m_e = 9.109383e-31
m_d = 2 * m_h

rm_h = (1 / ((1/m_e) + (1/m_h)))
rm_d = (1 / ((1/m_e) + (1/m_d)))

R_H = R_cons * (rm_h / m_e)
R_D = R_cons * (rm_d / m_e)

n1 = 2 
n2 = 3
n3 = 4
n4 = 5
n5 = 6

l_H1 = 1 / (R_H * ((1/n1)**2 - (1/n2)**2))
l_H2 = 1 / (R_H * ((1/n1)**2 - (1/n3)**2))
l_H3 = 1 / (R_H * ((1/n1)**2 - (1/n4)**2))
l_H4 = 1 / (R_H * ((1/n1)**2 - (1/n5)**2))

l_D1 = 1 / (R_D * ((1/n1)**2 - (1/n2)**2))
l_D2 = 1 / (R_D * ((1/n1)**2 - (1/n3)**2))
l_D3 = 1 / (R_D * ((1/n1)**2 - (1/n4)**2))
l_D4 = 1 / (R_D * ((1/n1)**2 - (1/n5)**2))

print(f'###     Hydrogen Balmer Series      ###\n')
print(f'#  First transition: {l_H1}')
print(f'# Second transition: {l_H2}')
print(f'#  Third transition: {l_H3}')
print(f'# Fourth transition: {l_H4}\n')

print(f'###     Deuterium Balmer Series     ###\n')
print(f'#  First transition: {l_D1}')
print(f'# Second transition: {l_D2}')
print(f'#  Third transition: {l_D3}')
print(f'# Fourth transition: {l_D4}\n')
