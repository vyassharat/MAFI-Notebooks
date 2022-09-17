"""
Author: Sharat Vyas
Assignment: Math 6204-Homework 1
Date: Completed on Septmber 15th

Use: This program values a series of European Call/Put options all at the
money. It illustrates how implied-vol changes the value of an option by keepeing
everything else the same and only varying the implied vol from .1 -> 1.The valuation is done in 2 forms.
The first approach is by using scipy's in built normal CDF functionality to compute the probabilites. The second
approach uses an approximation method to approximate the normal CDF. We then also diff the results and show that
the differences were nominal.

Files Included: We use 2 files, this one which is the driver(main.py)
and a file I created called european_option_pricer.py which has all the BSM pricing logic
"""

import numpy as np
from european_option_pricer import valueEuropeanOption

def main():
    # Define all constant parameters not changing for HW
    strike = 100
    underlying = 100
    div_yield = .025
    rate = .05
    start_time=0
    expiration_time=1
    imp_vol = np.array([.1, .2, .3, .4, .5, .6, .7, .8, .9, 1])

    # Compute Call/Put Option Price for each vol in the given list of vols
    for vol in imp_vol:
        valueEuropeanOption("Call",strike,underlying,start_time,expiration_time,div_yield,rate,vol)
        valueEuropeanOption("Put",strike,underlying,start_time,expiration_time,div_yield,rate,vol)


if __name__ == "__main__":
    main()