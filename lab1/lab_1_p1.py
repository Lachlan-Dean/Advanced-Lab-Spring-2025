import numpy as np
import scipy as sp

# This is part 1 of the first lab in Advanced Lab
# Titled: "Introduction to Programming in Python"


n, x, x2 = 0,0,0

# This piece will handle the running average
while True:
    try:
        line = float(input("Enter value: "))
    except:
        print("Data ended.")
        break
    
    n = n + 1
    x = x + line
    x2 = x2 + line**2

    print(n, " points: average = ", x / n)
    
# This piece will handle the running standard deviation

    if n == 1:
        print("Division by zero, enter more values")
    else:
        x_avg = x / n
        std2 = (x2 - n*(x_avg**2))/(n-1)
        print("Standard Deviation ", np.sqrt(std2))

