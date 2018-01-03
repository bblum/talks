#!/usr/bin/env python3

import numpy as np
import matplotlib
from importlib import import_module
import os.path
import sys
import argparse
import dateutil.parser
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange

# Work around matplotlib brain damage of binding backend at load
plt = None
def init_pyplot(nongraphical=False):
    global plt
    if nongraphical:
        matplotlib.use('Agg')
    plt = import_module("matplotlib.pyplot")
def write_pyplot(out):
    if out:
        plt.savefig(out)
    else:
        plt.show()

HEADER_NAMES = ["commit", "time", "pages", "word"]

def load_file(name):
    return matplotlib.mlab.csv2rec(name, names=HEADER_NAMES)

def make_graph(name):
    data = load_file(name)
    fig, ax = plt.subplots()

    ax.plot_date(data.time, data.pages)
#    ax.xaxis.set_major_locator(DayLocator())
 #   ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.set_ylim(0)
    ax.set_xlim(dateutil.parser.parse("2016-05-01")) # XXX
    plt.title('pages in thesis.pdf')
    fig.autofmt_xdate()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out")
    parser.add_argument("files", nargs='+')
    args = parser.parse_args()

    init_pyplot(args.out)
    make_graph(args.files[0])
    write_pyplot(args.out)

if __name__ == '__main__':
    sys.exit(main())
