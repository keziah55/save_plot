#!/usr/bin/env python3
""" Module to save/show matplotlib plots (SavePlot) or to save a legend as a
pdf (save_legend).

Checks if given file name already exists. If it does, asks if
you want to overwrite it or enter new name.
"""

import os
import sys
import numpy as np
import matplotlib.pyplot

class SavePlot():
    
    def __init__(self, save=False, savefile=None, mode='normal'):
        """
        Create SavePlot object.
        
        Parameters
        ----------
        * save : bool 
            If True, save the pdf. Otherwise show the plot.
            
        * savefile : string, optional
            File to which the plot should be saved.
            
        * mode : {'normal' 'quiet'}
            If quiet, suppress all messages to terminal. This will also
            automatically set auto_overwrite to True in plot().
        """
        
        self.save = save
        self.savefile = savefile
        self.mode = mode
        
    def _message(self, text):
        if self.mode == 'normal':
            print(text)
        
    def plot(self, plt, auto_overwrite=False, saveformat='pdf'):
        """ Show a matplotlib plot or save it as a pdf, then close the object.
            
            Parameters
            ----------
            * plt : matplotlib.pyplot object
                The object to plot
            * auto_overwrite : bool, optional
                If true, overwrites existing files without prompt. Otherwise
                asks for a new filename.
            * format : string
                Format in which to save plot (if saving)
        """
        
        if self.mode == 'quiet':
            auto_overwrite = True
        
        if self.save and self.savefile is None:
            self._message('Please give valid savefile')
            sys.exit(1)
        
        if self.save:
            if not auto_overwrite:
                try:
                    self.savefile = path_exists(self.savefile)
                except:
                    sys.exit(1)

            plt.savefig(self.savefile, format=saveformat)
            self._message('Saved {}'.format(self.savefile))
        else:
            plt.show()
            
        plt.close()
        
        
    def set_savefile(self, savefile):
        
        self.savefile = savefile
        
        
def save_legend(colours, labels, savefile, **kwargs):
    """ Save a matplotlib legend as a pdf (without a plot).
    
        Parameters
        ----------
        colours:
            list of colours
            
        labels:
            list of labels
            
        savefile:
            path to write legend.pdf to
        
        kwargs:
            matplotlib.pyplot.figlegend keyword arguments
    """
    
    x = np.arange(10)
    
    # create a figure for the data
    matplotlib.pyplot.figure()
    ax = matplotlib.pyplot.gca()
    
    for i in range(len(colours)):
        matplotlib.pyplot.plot(x, x * (i+1), colours[i], label=labels[i])
    
    # create a second figure for the legend
    figLegend = matplotlib.pyplot.figure(figsize = (3,2.5))
    
    # produce a legend for the objects in the other figure
    matplotlib.pyplot.figlegend(*ax.get_legend_handles_labels(), **kwargs)
    
    # save to file
    try:
        savefile = path_exists(savefile)
    except:
        sys.exit(1)
        
    figLegend.savefig(savefile, format='pdf')
    
    print('Saved {}'.format(savefile))
    
    
def path_exists(savefile):
    
    while os.path.exists(savefile):
        print('{} already exists. Would you like to overwrite it? '
              '[Y/n]'.format(savefile))
        ow = input()
        if ow.lower() == 'n':
            print('Please enter new file name: ')
            savefile = input()
        elif ow.lower() == 'y' or not ow:
            break
        elif ow.lower() != 'y':
            raise Exception('Invalid input. Aborting.')

    return savefile
