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
import abc

class SavePlt:
    
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, savefile=None, auto_overwrite=False, mode='normal',
                 saveformat='pdf'):
        """ Save a matplotlib legend as a pdf (without a plot).
        
            Parameters
            ----------
            * savefile : string
                path to write legend.pdf to
            
            * auto_overwrite : bool
                if file exists, overwrite without prompting.
                Note that if 'quiet' mode was selected, auto_overwrite will be
                True. Otherwise, defaults to False.
                
            * mode : {'normal', 'quiet'}
                If quiet, suppress all messages to terminal. This will also
                automatically set auto_overwrite to True in plot().
                
            * saveformat : string
                Format in which to save plot (if saving). Default is 'pdf'.

        """
        self.savefile = savefile
        self.auto_overwrite = auto_overwrite
        self.mode = mode
        self.saveformat = saveformat
        
        if self.mode == 'quiet':
            self.auto_overwrite = True
            
    def set_savefile(self, savefile):
        """ Set savefile """
        self.savefile = savefile
        
    def _message(self, text):
        if self.mode == 'normal':
            print(text)
    
    @staticmethod
    def path_exists(savefile):
        """ Check if a path exists. If it does, prompt to change/overwrite.
        
            Returns a path.
        """
        
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
            
class SavePlot(SavePlt):
    
    def __init__(self, save=False, savefile=None, auto_overwrite=False,
                 mode='normal', saveformat='pdf'):
        """ Create SavePlot object.
        
            Parameters
            ----------
            * save : bool 
                If True, save the pdf. Otherwise show the plot.
                
            * savefile : string, optional
                File to which the plot should be saved.
                
            * auto_overwrite : bool
                if file exists, overwrite without prompting.
                Note that if 'quiet' mode was selected, auto_overwrite will be
                True. Otherwise, defaults to False.
                
            * mode : {'normal', 'quiet'}
                If quiet, suppress all messages to terminal. This will also
                automatically set auto_overwrite to True in plot().
                
            * saveformat : string
                Format in which to save plot (if saving). Default is 'pdf'.
        """
        
        super().__init__(savefile, auto_overwrite, mode, saveformat)
        self.save = save
        
    def plot(self, plt):
        """ Show a matplotlib plot or save it as a pdf, then close the object.
            
            Parameters
            ----------
            * plt : matplotlib.pyplot object
                The object to plot
        """

        if self.save and self.savefile is None:
            self._message('Please give valid savefile')
            sys.exit(1)
        
        if self.save:
            if not self.auto_overwrite:
                try:
                    self.savefile = self.path_exists(self.savefile)
                except:
                    sys.exit(1)

            plt.savefig(self.savefile, format=self.saveformat)
            self._message('Saved {}'.format(self.savefile))
        else:
            plt.show()
            
        plt.close()
        
        
class SaveLegend(SavePlt):
        
    def save(self, labels, colours=None, linestyles=None, 
                    figsize=None, **kwargs):
        """ Save a matplotlib legend as a pdf (without a plot).
        
            Parameters
            ----------
            * savefile : string
                path to write legend.pdf to
                
            * labels : list
                list of labels
                
            * colours : list
                list of colours. If None, black will be used for all.
            
            * linestyles : list
                list of linestyles. If None, solid line will be used for all.
                
            * figsize : tuple
                tuple of wisth and height (inches) of output figure. 
                If None, will be set to rc.figure.figsize.
            
            * kwargs :
                matplotlib.pyplot.figlegend keyword arguments
                `loc` is set to 'center', but other kwargs, such as `ncol` are
                available
        """

        # create a figure for the data
        fig = matplotlib.pyplot.figure()
        ax = matplotlib.pyplot.gca()
        
        if colours is None and linestyles is None:
            raise RuntimeError('Please provide a list of colours and/or linestyles.')
                
        # if colours/linestyles not provided, use black/solid line for all
        if colours is None:
            colours = ['black'] * len(labels)
        if linestyles is None:
            linestyles = ['-'] * len(labels)
            
        x = np.arange(10)
        
        for i in range(len(colours)):
            matplotlib.pyplot.plot(x, x * (i+1), colours[i], label=labels[i], 
                                   linestyle=linestyles[i])
        
        # create a second figure for the legend
        figLegend = matplotlib.pyplot.figure(figsize=figsize)
        
        # produce a legend for the objects in the other figure
        # loc is a required argument, but makes no difference when only the legend is being displayed
        matplotlib.pyplot.figlegend(*ax.get_legend_handles_labels(), 
                                    loc='center', **kwargs)

        if not self.auto_overwrite:
            try:
                self.savefile = self.path_exists(self.savefile)
            except:
                sys.exit(1)

        figLegend.savefig(self.savefile, format=self.saveformat)
        
        self._message('Saved {}'.format(self.savefile))
        
        matplotlib.pyplot.close(fig)
        matplotlib.pyplot.close(figLegend)
    
