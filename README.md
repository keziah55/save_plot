# SavePlot - Python module for easily displaying or saving matplotlib plots.

I often have to switch between showing and saving plots when working. This can be a 
faff when the plt.show()/plt.savefig() commands are at the end of the script, so 
occasionally I've accidentally overwritten a graph or run something only to find I forgot
to tell it to save the graph.

SavePlot allows you to create a SavePlot object, telling it whether to save (`True`) or 
show (`False`) the figure.
Then, when the actual plotting is required, you simply call SavePlot.plot(plt).

When saving, if the file already exists, SavePlot will prompt you to overwrite/rename.
This behaviour can be overridden by setting `auto_overwrite=True` in the SavePlot.plot args.
The default format is pdf. This can also be changed in the SavePlot.plot args.

Output to stdout can be supressed by stating `mode='quiet'` when creating the object.


## Example - saving a plot
```python

import matplotlib.pyplot as plt
import numpy as np
from save_plot import SavePlot

# make SavePlot object which will save the figure
sp = SavePlot(True, 'test.pdf')

##############
## do stuff ##
##############

plt.plot(x,y)

# save the plot
# if the file already exists, overwrite without prompting
sp.plot(plt, auto_overwrite=True)

```



## save_legend

saveplot.py also contains a function called save_legend which allows you to save just
a legend when given a list of colours and labels.


## Installing

SavePlot requires Python3 and the corresponding versions of NumPy and Matplotlib.

```
python setup.py build_ext

sudo python setup.py install
```


