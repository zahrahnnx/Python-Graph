import pandas as pd
import matplotlib.dates as dates

def custom_date_formatter(x, pos):
    date = dates.num2date(x)
    if date.day == 1 or date.day == 15:
        return date.strftime('%d')
    else:
        return ''
    

def read_myfile(filename):
    AutaugaLoc = pd.read_csv(filename, sep=",", index_col=0)
    return AutaugaLoc