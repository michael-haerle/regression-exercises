import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd
import seaborn as sns
from math import sqrt

import sklearn.preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score
from sklearn.feature_selection import f_regression 
from sklearn.metrics import mean_squared_error


import os
import env
import wrangle

def regression_errors(y, train_scaled):
    MSE = mean_squared_error(y, train_scaled.yhat)
    SSE = MSE * len(train_scaled)
    RMSE = MSE**.5
    ESS = sum((train_scaled.yhat - y.mean())**2)
    TSS = ESS + SSE
    print('SSE =', "{:.2f}".format(SSE))
    print(f'MSE = {MSE:.2f}')
    print("RMSE = ", "{:.2f}".format(RMSE))
    print("ESS = ", "{:.2f}".format(ESS))
    print("TSS = ", "{:.2f}".format(TSS))

def baseline_mean_errors(y, train_scaled):
    MSE_baseline = mean_squared_error(y, train_scaled.yhat_baseline)
    SSE_baseline =  MSE_baseline * len(train_scaled)
    RMSE_baseline = MSE_baseline**.5
    print("SSE Baseline =", "{:.2f}".format(SSE_baseline))
    print(f"MSE Baseline = {MSE_baseline:.2f}")
    print("RMSE Baseline = ", "{:.2f}".format(RMSE_baseline))

def better_than_baseline(y, train_scaled):
    MSE = mean_squared_error(y, train_scaled.yhat)
    SSE = MSE * len(train_scaled)
    RMSE = MSE**.5
    ESS = sum((train_scaled.yhat - y.mean())**2)
    TSS = ESS + SSE
    MSE_baseline = mean_squared_error(y, train_scaled.yhat_baseline)
    SSE_baseline =  MSE_baseline * len(train_scaled)
    RMSE_baseline = MSE_baseline**.5
    if SSE_baseline < SSE:
        print('SSE_baseline is better')
    else:
        print('SSE is better')
    if MSE_baseline < MSE:
        print('MSE_baseline is better')
    else:
        print('MSE is better')
    if RMSE_baseline < RMSE:
        print('RMSE_baseline is better')
    else:
        print('RMSE is better')