import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.umath import *


hah = ufloat(656.03803519816070, 2.6545550721472702e-05)
had = ufloat(655.85955309185590, 1.0780232020319136e-05)

hbh = ufloat(485.84041437584017, 5.4355348677436480e-05)
hbd = ufloat(485.70892633443407, 7.8902406825743370e-05)

hgh = ufloat(433.75598310720700, 4.2794547655374924e-05)
hgb = ufloat(433.63804843891050, 2.3077468535667013e-05)

hdh = ufloat(409.87990835727260, 2.5034589177402170e-05)
hdb = ufloat(409.76839556061330, 2.5129853655541310e-05)

print('H-Alpha Isotope Shift: ', hah-had)
print('H-Beta Isotope Shift:  ', hbh-hbd)
print('H-Gamma Isotope Shift: ', hgh-hgb)
print('H-Delta Isotope Shift: ', hdh-hdb)
