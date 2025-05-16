import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# This code will involve plotting a Poisson distribution and a Gaussian distribution.
# Gaussian is continuous; Poisson is discrete. 


mu = 20
sigma = np.sqrt(mu)

# For a Gaussian, it will look continuous, so this will act as an array
# of a lot of closely bunched points. The y1 arrary pairs with the x1 array,
# with sigma referring back to our initialized variable above

num = 500
x1 = np.linspace(0, 30, num=num)
y1 = 1./(np.sqrt(2 * np.pi) * sigma) * np.exp(-(x1-mu)**2/2./sigma/sigma)

# Poisson distrib is only on positive integers and zero.
x2 = np.arange(10,29,1,dtype=int)
y2 = np.exp(-mu) * (mu**x2)/sp.special.factorial(x2,exact=False)

plt.figure(1)
# The first 2 numbers are a matrix configuration, and the last is
# which plot in the matrix to make.
plt.subplot(211)
p1 = plt.plot(x1, y1, 'k', label = 'Gaussian') # ’k’: black; line is assumed.
p2 = plt.plot(x2, y2, '*', label = 'Poisson') # ’*’: points are stars
plt.xlabel('x axis label')
plt.ylabel('y label')
plt.legend()
plt.title('mu = 20 plots')
plt.subplot(212)

# The second plot is made to sit below the first

p2 = plt.plot(x2, y2, 'x', label = 'Poisson') 
plt.show()
