import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

t, pd1, pd2, err, temp, laser = np.genfromtxt('LaChris-data-Feb13-25LW2P.txt', unpack=True)
v, theta, theta_diff = np.genfromtxt('data_p2b.txt', unpack=True)


# Defining fitter function for Malus' Law
def func(theta, p):
    theta_rad = np.radians(theta)
    z = p[0] * np.cos(theta_rad - p[1])**2 + p[2]
    return z

def errfunc(p, x, y, err):
    return(y - func(x,p)) / err

sig = np.array([0.002, 0.002, 0.002, 0.002,
    0.002, 0.002, 0.002, 0.002, 0.002,
    0.002, 0.002, 0.002, 0.002, 0.002,
    0.002, 0.002, 0.002, 0.002, 0.002])

p0 = [0.5, 90, 0.8]

out = sp.optimize.leastsq(errfunc,
        p0,
        args=(theta, v, sig),
        full_output=1)

pfinal = out[0]  # final fit params
covar = out[1]   # covariance matrix - sqrt(diagonal) ˜ unc per param
mydict = out[2]  # dict, includes weighted resids (list), key=’fvec’
mesg = out[3]    # message from fitter
ier = out[4]     # error flag: success if 1, 2, 3, or 4 (or check covar)
resids = errfunc(pfinal, theta, v, sig)
chisq = np.sum(resids**2)
degs_frdm = len(theta)-len(pfinal) # degrees of freedom
reduced_chisq = chisq/degs_frdm

print('Fitter status: ', ier, ' -- aka -- ', mesg)
i = 0
if covar is not None:
    for u in pfinal:
        print(f'Param {i+1}: {u:.2f} +/- {np.sqrt(covar[i,i]):.2f}')
        i = i+1
    print(f'Reduced chisq {reduced_chisq:.2f}')
else:
    print('Fitter failed (no covariance matrix).')


xfit = np.linspace(90, 280, 19)
yfit = pfinal[0] * np.cos(np.radians(xfit) - pfinal[1])**2 + pfinal[2]

figure, axis = plt.subplots(1, 2, sharex=False, figsize=(10,5))

# Time vs Laser plot
#axis[0,0].plot(t,laser, scalex=True)
#axis[0,0].set_title("Time vs Laser Power")

#axis[0,1].plot(theta, v)
#axis[0,1].set_title("Angle vs DVM Reading")

axis[0].scatter(theta, v)
axis[0].plot(xfit, yfit)
axis[0].set_title("Scatter Angle vs DVM Reading with Malus' Law Fit")

axis[1].plot(xfit, yfit)
axis[1].set_title("Malus' Law Fit Plot")

plt.show()
