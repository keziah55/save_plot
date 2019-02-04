# SavePlot - Python module for displaying or saving matplotlib plots.

(C) Keziah Milligan, 2017
GPL v3. See https://www.gnu.org/licenses/gpl-3.0.en.html

I often have to switch between showing and saving plots when working. This can be a 
faff when the plt.show()/plt.savefig() commands are at the very end of the script and
the parameters I'm changing are at the top.
Occasionally I've accidentally overwritten a graph or leave a huge program to run to a while, 
only to find I forgot to tell it to save the graphs it generates.

SavePlot allows you to create a SavePlot object, telling it whether to save (`True`) or 
show (`False`) the figure.
Then, when the actual plotting is required, you simply call `SavePlot.plot(plt)`.

When saving, if the file already exists, SavePlot will prompt you to overwrite/rename.
This behaviour can be overridden by setting `auto_overwrite=True` in the constructor.
Output to stdout can be supressed by stating `mode='quiet'`.

save_plot.py also includes an object which will create a stand-alone legend, `SaveLegend`.
The constructor is identical to that of SavePlot (except it will always save the output: 
no boolean is needed). `SaveLegend.plot` takes a list of labels and colours and/or linestyle
and any other `matplotlib.pyplot.figlegend` keyword arguments.

All figures will be saved as PDFs, with metadata set by SavePlot. 
The user name and the name of the Python script which called SavePlot are set as the PDF 
author and subject, respectively.


## Example - saving a plot
```python

import matplotlib.pyplot as plt
import numpy as np
from save_plot import SavePlot

# make SavePlot object which will save the figure
sp = SavePlot(True, 'test.pdf', auto_overwrite=True)

x = np.linspace(0, 2*np.pi, num=1000)
y = np.sin(x)

plt.plot(x,y)

# save the plot
sp.plot(plt)

```

Also see `example.py` for a demonstration of both `SavePlot` and `SaveLegend`.



## Installing

SavePlot requires Python 3.x and the corresponding versions of NumPy and Matplotlib. 

As you would expect, it can be installed with:
```
python setup.py build_ext

sudo python setup.py install
```


