# SavePlot - Python module for easily displaying or saving matplotlib plots.

I often have to switch between showing and saving plots when working. This can be a 
faff when the plt.show()/plt.savefig() commands are at the end of the script, so 
occasionally I've accidentally overwritten a graph or run something only to find I forgot
to tell it to save the graph.

SavePlot allows you to create a SavePlot object, telling it whether to save or show the figure.
Then, when the actual plotting is required, you simply call SavePlot.plot(plt).


## Example
```python

import matplotlib.pyplot as plt
import numpy as np
from save_plot import SavePlot

# make SavePlot object which will save the figure
sp = SavePlot(True, 'test.pdf')

x = np.linspace(0, 2*np.pi, 1000)

y = np.sin(x)

plt.plot(x,y)

# save the plot
# if the file already exists, prompt to overwrite/rename
sp.plot(plt, auto_overwrite=False)

```



## Installing

SavePlot requires Python3 and the corresponding versions of NumPy and Matplotlib.

```
python setup.py build_ext

sudo python setup.py install
```


