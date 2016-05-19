import numpy as np
import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.
labels = ['Delivered power', 'Low-energy filter', 'Thermalization', 'High-energy filter']
sizes = [28.08, 21.51, 12.73, 37.68]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'violet']
explode = (0.1, 0, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')

plt.rcParams['font.size'] = 20.0

plt.text(-1.1, 1, 'Gain', size=32)
plt.text(0.7, -1, 'Losses', size=32)

# set labeldistance=11 to large value: do not show labels on pie plot
plt.pie(sizes, explode=explode, labels = labels, colors=colors, autopct='%1.2f%%', shadow=True, startangle=90, labeldistance=11)

plt.legend(prop={'size':17.5}, loc=(0.6,0.8))

# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

plt.savefig('pie_cart2.pdf')
plt.show()
