from pydataset import data as dataset
from sklearn import linear_model, neural_network, metrics
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from prettyprinter import cpprint as pp

import pandas_profiling
import numpy as np  
import pandas as pd  
import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

df = dataset('airquality')

profile = pandas_profiling.ProfileReport(df)
profile.to_file('report.html')
rejected_variables = profile.get_rejected_variables(threshold=0.8)

print(rejected_variables)

target = ['Ozone']

df = df.dropna(axis=0)
y = df[target]
df = df.drop(target, axis=1)
df = df.drop(rejected_variables, axis=1)

# X = pd.get_dummies(df) # In the case of categorical variables: use one-hot encoding

scaler = StandardScaler()
X = scaler.fit_transform(df)
y = np.ravel(scaler.fit_transform(y))

X_train, X_test, Y_train, Y_test = train_test_split(
    X, y, test_size=.20, random_state=2)

pp({'Type': 'Regression', 'Model': 'MLPRegression', 'Predictors': df.columns.values.tolist(), 'Target': target, 'Size': df.shape[0], 'Training%': 80})


hyperparameters = [{'hidden_layer_sizes': [[40, 40], [30, 30, 30], [20, 20, 20, 20]],
                     'activation': ['relu'],
                     'solver':['adam', 'lbfgs'], 'alpha':[0.0001],
                     'batch_size':['auto'], 'learning_rate':['constant'],
                     'learning_rate_init':[0.0001], 'max_iter':[5000], 'random_state':np.arange(100)}]

model = GridSearchCV(neural_network.MLPRegressor(),
                   hyperparameters, scoring='r2', verbose=1, n_jobs=8, cv=5)

# model = linear_model.LinearRegression().fit(X_train, Y_train)

model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)

pp(model.best_params_)

# pp({'Best Training Score': model.best_score_})

pp({'Mean Absolute Error': metrics.mean_absolute_error(Y_test, Y_pred), 
    'Mean Squared Error': metrics.mean_squared_error(Y_test, Y_pred),
    'Root Mean Squared Error': np.sqrt(metrics.mean_squared_error(Y_test, Y_pred)),
    'R^2': metrics.r2_score(Y_test, Y_pred, multioutput='variance_weighted')})

