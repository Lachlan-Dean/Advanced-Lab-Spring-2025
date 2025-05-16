import numpy as np 

# This is part 2 of the first lab in Advanced Lab
# This part will deal with inputting sets of data and 
# reading them to find the average and standard deviation

#a = np.genfromtxt("1D_data.txt")
a = [2.40, 2.45, 2.47, 3.13, 2.92, 2.85, 2.05, 2.52, 2.94, 1.89, 1.94, 1.55, 2.12, 2.17, 2.17, 3.06, 1.97, 2.23, 3.2, 2.24]

n,x, x2 = 0,0,0

for array_element in a:
    n = n + 1 
    x = x + array_element
    x2 = x2 + array_element**2

print(n, " points: average = ", x / n)
x_avg = x / n 
print("Standard deviation with ", n, " points: ", np.sqrt((x2 - n*(x_avg**2))/(n-1)))

print("Numpy mean: ", np.mean(a))
print("Numpy standard deviation: ", np.std(a, ddof=1))
