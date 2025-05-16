import numpy as np
import scipy as sp
from scipy.special import factorial
from scipy.stats import poisson
import matplotlib.pyplot as plt

samples, counts = np.genfromtxt('20250219.out', unpack=True)

tcounts = np.sum(counts)
tsamples = len(samples)

avg_count = np.mean(counts)
avg_ctpsam = tcounts / tsamples

print('Total counts: ', tcounts)
print('Total samples: ', tsamples)
print('Average count per sample: ', avg_ctpsam)
print('Square root of average: ', np.power(avg_ctpsam, 0.5))
print('Standard Deviation: ', np.std(counts))

# Code from Chris
def create_plot(bin_size):
    plt.figure=((10,6))
    bins = range(int(np.min(counts)), int(np.max(counts)) + bin_size,bin_size)
    hist, bins, _ = plt.hist(counts, bins, edgecolor='k')

bin_size = 2

x = np.arange(0, int(np.max(counts))+1, 0.1)
poisson_line = (np.exp(-avg_count) * np.power(avg_count, x)) / factorial(x)
scaled_poisson = poisson_line * len(samples)*bin_size
# end of code from Chris


figure, axis = plt.subplots(1, 1, sharex=True, figsize=(10,10))
plt.plot(x, scaled_poisson)
plt.xlabel('Counts')
plt.ylabel('Frequency')
create_plot(bin_size)

plt.show()
