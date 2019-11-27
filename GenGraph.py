#!/path/to/python3
'''
  Author:   Ricky Martinez
  Purpose:  This file serves as a Python EQUIVALENT to the old GenGraph file which is written in PHP.
            Every function should written to return a boolean (True, False).
            Questions about usage? Use the GenIPScanGraph function as an example

            
            Check if __name__ == "__main__" function
'''

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import os

def GenIPScanGraph(device, date_info, ipscan_info):
    fig = plt.figure(frameon=False)                                   # Create a reference to the figure.
    ax = plt.subplot()                                                # Create a reference to axis.
    ax.spines['top'].set_visible(False)                               # Set only bottom and left axis as visisble
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)
    ax.grid(color='lightgrey', linestyle='-', linewidth=1)            # Create gridlines on the graph

    plt.title(device)                                                 # Set the title for the graph

    for axis in [ax.xaxis, ax.yaxis]:                                 # Make only full numbers (Integers) display.
        axis.set_major_locator(ticker.MaxNLocator(integer=True))

    ymin = min(ipscan_info)-2                                         # Set min and max value from y-axis.
    ymax = max(ipscan_info)+2
    ax.set_ylim([ymin, ymax])
    plt.ylabel('IP Scan Number')                                      # Set label for y-axis

    plt.xlabel('Date')                                               # Set label for x-axis
    plt.xticks([i for i in range(len(date_info))],date_info)         # Set x-ticks
    plt.xticks(rotation=60)
    plt.xticks(fontsize=8)

    plt.plot(ipscan_info)                                             # Plot the data

    plt.tight_layout()                                                # Specifies a tight layout to avoid x,y -labels being cut off.
    filename = '/path/to/img/dir.IPScanGraph.png'     # Specify which file the img will be saved to
    try:                                                              # Exception handler: if the file is successfully saved, return True
        fig.savefig(filename)
        return True
    except Exception as e:                                            # If the file is not successfull saved, return False
        return False;

if __name__ == "__main__":
    '''
        This is a TEST. This script will only really be called from other webpages.
        It should only be called by itself in instances of a test.
    '''
    print("[ TESTING MODE ]")
    status = GenIPScanGraph("TESTENV", ['12-01', '12-02', '12-03', '12-04'], [643, 643, 643, 6])

    if status:
        print("[ DONE ]")
    else: print("[ FINISHED WITH ERRORS ]")
