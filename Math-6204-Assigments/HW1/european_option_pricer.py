# -*- coding: utf-8 -*-
"""
This file contains all the logic to value a European Call/Put option using Black-Scholes and
it's given parameters.
"""

#Imports
import numpy as np
import math
from scipy.stats import norm

#Constants Used for Approximation Approach
A1 = 0.319381530
A2 = -0.356563782
A3 = 1.781477937
A4 = -1.821255978
A5 = 1.330274429


#Method called by user returns the value of a call/put
def valueEuropeanOption(type,strike,underlying,initial_time, terminal_time, div_yield, rate, vol):
    ttm = terminal_time-initial_time
    if(type=="Call"):
        price,approximatedPrice = compute_call(strike, underlying, ttm, vol, div_yield, rate)
    else:
        price,approximatedPrice = compute_put(strike, underlying, ttm, vol, div_yield, rate)

    print("\nOption Params")
    print("***********************************")
    print("Option Type: " + type)
    print("S:" + str(underlying))
    print("K:" + str(strike))
    print("Initial Time:" + str(initial_time))
    print("Terminal Time: " + str(terminal_time))
    print("Div Yield: " + str(div_yield))
    print("Risk Free Rate: " + str(rate))
    print("Vol:" + str(vol))
    print("***********************************")
    print("Price -> $" + str(price))
    print("Approximated Price -> $" + str(approximatedPrice))
    print("Difference -> $" + str(np.abs(price - approximatedPrice)))
    print("***********************************")
    return price,approximatedPrice
    
#Computes Call using Scipy CDF and Approximation Approach
def compute_call(strike, underlying, TTM, imp_vol, div_yield, rate):
    #Computes D1/D2 and uses them for both call value approaches
    d1 = compute_d1(underlying, strike, rate, div_yield, imp_vol, TTM)
    d2 = compute_d2(d1,imp_vol, TTM)

    call_price = (underlying * np.exp(-1*div_yield*TTM)*norm.cdf(d1))
    call_price -= (strike*np.exp(-1*rate*TTM)*norm.cdf(d2))

    approximatedCallPrice = (underlying * np.exp(-1*div_yield*TTM)*approximateNormCDF(d1))
    approximatedCallPrice -= (strike*np.exp(-1*rate*TTM)*approximateNormCDF(d2))

    return call_price,approximatedCallPrice

#Computes Put using Scipy CDF and Approximation Approach
def compute_put(strike, underlying, TTM, imp_vol, div_yield, rate):
    # Computes D1/D2 and uses them for both put value approaches
    d1 = compute_d1(underlying, strike, rate, div_yield, imp_vol, TTM)
    d2 = compute_d2(d1,imp_vol, TTM)

    put_price = -1*(underlying * np.exp(-1*div_yield*TTM)*norm.cdf(-1*d1))
    put_price += (strike*np.exp(-1*rate*TTM)*norm.cdf(-1*d2))

    approximatedPutPrice = -1*(underlying * np.exp(-1*div_yield*TTM)*approximateNormCDF(-1*d1))
    approximatedPutPrice += (strike*np.exp(-1*rate*TTM)*approximateNormCDF(-1*d2))

    return put_price,approximatedPutPrice

def approximateNormCDF(value):
    # This method is what is used to help alleviate when a negative value is passed in
    if(value<0):
        return 1 - standardNormalCumulativeDistribution(-1*value)
    else:
        return standardNormalCumulativeDistribution(value)

#Returns approximation to Standard normal CDF
def standardNormalCumulativeDistribution(value):
    return 1-standardNormalPDF(value)*z(value)*((((A5*z(value) + A4)*z(value)+A3)*z(value)+A2)*z(value)+A1)

#Returns value of Standard normal pdf
def standardNormalPDF(value):
    return (1/np.sqrt(2*math.pi))*np.exp(-1*(value**2)/2)

#Helper function for approximation approach
def z(value):
    return 1/(1+0.2316419*value)

#Used to centralize computations for D1
def compute_d1(S,K,r,delta,sigma,TTM):
    numerator = np.log(S/K)+(r-delta+((sigma**2)/2)*TTM)
    denominator = sigma*np.sqrt(TTM)

    return numerator/denominator

#Used to centralize computations for D2
def compute_d2(d1,sigma,TTM):
    return d1-sigma*np.sqrt(TTM)
