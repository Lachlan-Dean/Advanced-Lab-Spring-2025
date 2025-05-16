import numpy as np
import matplotlib.pyplot as plt


# This is part 3 of the first lab in Advanced Lab

# Part 1 
a = np.random.normal(5.0, 1.0, 1000)
b = np.random.normal(12.0, 1.5, 1000)
c1 = a * b


print(np.mean(c1), np.std(c1, ddof=1))


# Part 2
a = np.random.normal(50.0, 5.0, 1000)
b = np.random.normal(5.0, 1.0, 1000)
c2 = a * np.exp(b)

print(np.mean(c2), np.std(c2, ddof=1))

plt.figure()
plt.hist(c2, 100, range=(0, 50000))
#plt.hist(c1, 100, range=(0, 50000))
# plt.hist(a, 100, range(min, max)) makes 100 bins between min and max
plt.show()


'''
a = 50
b = 5

print(a * np.exp(b))
print(np.sqrt((a * np.exp(b) * 5)**2 + (a * np.exp(b) * 1.5)**2))
'''




