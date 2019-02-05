"""
Example file to show the use of SavePlot and SaveLegend.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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
labels = list('{} rad/s'.format(f) for f in freq)

# using seaborn style
# feel free to omit this
sns.set_style('darkgrid')

# plot some waves
for idx, f in enumerate(freq):
    plt.plot(x, amp[idx]*np.sin(f*x), color=c[idx], linestyle=ls[idx])
    
# label axes
plt.ylabel('sin(x)')
plt.xlabel('x (rad)')

# set x-axis ticks and labels in fractions of pi
# (I'm simply leaving some labels blank to aviod the hassle of proper 
# matplotlib ticker stuff)
xtx = np.linspace(0, 2*np.pi, 9)
pi = '\u03c0'
xtxlab = ['0', '', '{}/2', '', '{}', '', '3{}/2', '', '2{}']
xtxlab = [item.format(pi) for item in xtxlab]
plt.xticks(ticks=xtx, labels=xtxlab)

# save the plot
sp.plot(plt)

# save the legend
sl.plot(labels, colours=c, linestyles=ls, markers=mk, figsize=(2,2), ncol=1)
