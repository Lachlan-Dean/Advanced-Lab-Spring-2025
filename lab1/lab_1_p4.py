import numpy as np
import matplotlib.pyplot as plt

# This is part 4 of the first lab in Advanced Lab
try:
    fin = 'ibex_0109.txt'
    a = np.genfromtxt(fin)
except:
    print("file not found, where is it?")
    quit()

#fin.close()


x = np.linspace(0, 59, num=60)


plt.plot(x, a[:,2],
        color='green', label='Energy 2')
plt.title('IBEX ESA 2 and 3')
plt.ylabel('count rate (/s)')
plt.xlabel('angle bin')


# plotting error bar
plt.errorbar(x, a[:,4], yerr=a[:,5], xerr=None,
    color='blue', fmt='s', label='Energy 3')

# This line sets the y-axis to log scale
#plt.yscale('log')

plt.ylim(ymin=0)
plt.legend()

plt.show()

