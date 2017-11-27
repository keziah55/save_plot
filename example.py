"""
Example file to show the use of SavePlot and SaveLegend.
"""

import numpy as np
import matplotlib.pyplot as plt
from save_plot import SavePlot, SaveLegend

# make save_plot objects
sp = SavePlot(True, 'waves.pdf')
sl = SaveLegend('legend.pdf', auto_overwrite=True)

# parameters for sine waves
x = np.linspace(0, 2*np.pi, 1000)
freq = np.arange(1,5)
amp = [0.5, 1, 0.75, 0.25]

# colours, linestyles and labels
c = ['darkorange','dodgerblue', 'firebrick', 'green']
ls = ['-', '--', ':', '-.']
mk = ['o', None, None, None]
labels = list('{}Hz'.format(f) for f in freq)

# plot some waves
for idx, f in enumerate(freq):
    plt.plot(x, amp[idx]*np.sin(f*x), color=c[idx], linestyle=ls[idx])
    
# add stuff to the plot
plt.grid()
plt.ylabel('sin(x)')
plt.xlabel('x')

# save the plot
sp.plot(plt)

# save the legend
sl.save(labels, colours=c, linestyles=ls, markers=mk, figsize=(1,1), ncol=1)
