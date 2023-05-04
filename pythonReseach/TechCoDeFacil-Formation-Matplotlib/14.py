#-*-encoding:utf8-*-
#  candlestick OHLC graphs
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib import style

style.use('dark_background')
print(plt.style.available)
print(plt.__file__)

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


with open('tsla.csv', 'r') as csvfile:
    fig = plt.figure('figure one')
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    # ax1.grid(True, color='g', linestyle='-', linewidth=0.1)

    source_code = csvfile.read()
    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'Date' is not line and 'Close' not in line:
                stock_data.append(line)

    date, openp, hightp, lowp, closep, aclosep, volume = np.loadtxt(stock_data,
                                                                    delimiter=',',
                                                                    unpack=True,
                                                                    converters={0: bytespdate2num('%Y-%m-%d')})

    ax1.plot(date, closep, label='close Price')
    ax1.plot(date, openp, label='close Price')

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.grid(True)

    plt.xlabel('dates')
    plt.ylabel('close price')
    plt.title('finance with python  matplotlib')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()