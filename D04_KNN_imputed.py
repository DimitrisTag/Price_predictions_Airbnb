# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 15:54:09 2021

@author: leontaridiss
"""

import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import Lasso, Ridge
from sklearn.impute import KNNImputer

df = pd.read_csv('knn_imputed.csv')


y = (df['price'])
df.drop(['price'],axis=1,inplace=True)
X = df



def cross_val(scaler, model ,name):
    cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=40)
    pipe = Pipeline([('imputer', KNNImputer()), ('scaler', scaler),('model', model)])
    scoresMAE = cross_val_score(pipe, X, y,cv = cv,scoring = 'neg_mean_absolute_error')
    scoresR2 = cross_val_score(pipe, X, y,cv = cv,scoring='r2')
    print(name,": %0.2f MAE, %0.2f R2" % (scoresMAE.mean(), scoresR2.mean()))

print('Pipeline with StandardScaler\n')
cross_val(StandardScaler(), XGBRegressor(), 'XGB')
cross_val(StandardScaler(), LinearRegression(), 'LinReg')
cross_val(StandardScaler(), RandomForestRegressor(), 'RandomForest')
cross_val(StandardScaler(), Lasso(alpha=0.1), 'Lasso')
cross_val(StandardScaler(), Ridge(alpha=1.0), 'Ridge')
cross_val(StandardScaler(), GradientBoostingRegressor(), 'GradientBoostingRegressor')
print('\n')
print('Pipeline with MinMaxScaler\n')
cross_val(MinMaxScaler(), XGBRegressor(), 'XGB')
cross_val(MinMaxScaler(), LinearRegression(), 'LinReg')
cross_val(MinMaxScaler(), RandomForestRegressor(), 'RandomForest')
cross_val(MinMaxScaler(), Lasso(alpha=0.1), 'Lasso')
cross_val(MinMaxScaler(), Ridge(alpha=1.0), 'Ridge')
cross_val(MinMaxScaler(), GradientBoostingRegressor(), 'GradientBoostingRegressor')























