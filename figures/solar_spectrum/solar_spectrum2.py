import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(0,8,2000)

plt.rcParams['axes.linewidth'] = 2 #set the value globally

fig = plt.figure(figsize=(12,10))
ax = plt.subplot(111)

plt.plot(w, 100*w**3/(np.exp(w/0.5066)-1), 'k-', linewidth = 5)
plt.axvline(1.1, color='r', linestyle='-', linewidth = 2.0)
plt.axvline(2.1, color='b', linestyle='--', linewidth = 2.0)

# fill between two lines
plt.axvspan(0.0, 1.1, alpha = 0.5, color='gold')
plt.axvspan(1.1, 2.1, alpha = 0.5, color='yellowgreen')
plt.axvspan(2.1, 8.5, alpha = 0.5, color='violet')
#'yellowgreen', 'lightskyblue'

# We change the fontsize of minor ticks label 
plt.tick_params(axis='both', which='major', labelsize=20)

plt.xlabel("Photon energy $w$, eV", fontsize = 25)
plt.ylabel("Power density, arb. units", fontsize = 25)

ax.tick_params(width=2, size = 7)

plt.text(0.3, 20.5, 'Gap energy', color = 'Red', size=25)
plt.text(2.5, 18, 'High-energy filter', color = 'Black', size=25)
plt.text(0.2, 18, 'Filter', color = 'Black', size=25)

plt.xlim(xmax = 8.0)
plt.savefig("Planck-spectrum2.pdf")

plt.show()
