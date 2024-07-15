# Import libraries
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as dates
from matplotlib.ticker import FuncFormatter
from plot_utils import read_myfile, custom_date_formatter
    
def plot_data(filename):
    mydata = read_myfile(filename)
    # Convert index to datetime
    idx=pd.to_datetime(mydata.index, format='%m/%d/%y')
    # Create series with datetime index
    s = pd.Series(mydata['Autauga'].values, index=idx)


    ax = plt.figure(figsize=(20,6), dpi=72).add_subplot(111)
    ax.plot_date(idx.to_pydatetime(), s, '-')

    # Set minor and major locator and formatter
    ax.xaxis.set_minor_locator(dates.DayLocator())
    ax.xaxis.set_minor_formatter(FuncFormatter(custom_date_formatter))
    ax.xaxis.set_major_locator(dates.MonthLocator())
    ax.xaxis.set_major_formatter(dates.DateFormatter('%b\n%Y')) #or '\n\n\n%b\n%Y'
    # ax.xaxis.grid(True, which="minor")

    plt.title('Daily change in Covid-19 Confirmations')
    plt.xlabel('Date')
    plt.ylabel('Daily Changes')

   # Set ticks size and labels
    ax.tick_params(axis='x', which='minor', labelsize=8, length=5, pad=10)
    ax.tick_params(axis='x', which='major', labelsize=10, length=8, pad=20)
    ax.yaxis.grid()
    plt.tight_layout()

    # Highlight the 15th with a longer tick
    for tick in ax.get_xaxis().get_minor_ticks():
        if tick.label1.get_text() == '15':
            tick.tick1line.set_markersize(8)  # Increase the size of the tick on the 15th

    plt.show()

