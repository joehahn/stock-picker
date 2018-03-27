#!/usr/bin/env python

#train.py
#
#by Joe Hahn
#jmh.datasciences@gmail.com
#26 March 2018
#
#this preps the historical data that the model will be trained on 

#to execute:
#    ./train.py

#set input parameters
start_date = '2013-01-01'
end_date = '2016-07-01'
debug = True

#read list of preferred tickers
import pickle
file = 'data/selected_tickers.pkl'
with open(file) as f:
    tickers = pickle.load(f)
if (debug):
    print 'number of preferred tickers = ', len(tickers)

#get each ticker's opener
file = 'data/openers.pkl'
with open(file) as f:
    openers = pickle.load(f)
if (debug):
    print openers.head()

#read and prep NYSE data
from stock_picker_source.helper_fns import *
xy, xcols, ycol = prep_xy(start_date, end_date, tickers, openers, debug=debug)

#extract the x features
cols = []
for col in xy.columns:
    for s in xcols:
        if (col.startswith(s)):
            cols += [col]
x = xy[cols]
x_array = x.values
if (debug):
    print x.head()
    print 'x.shape = ', x.shape
    print 'x_array.shape = ', x_array.shape
    print [col for col in x.columns if ('_GE' in col)]

#extract the target variables y
cols = []
for col in xy.columns:
    for s in [ycol]:
        if (col.startswith(s)):
            cols += [col]
y = xy[cols]
y_array = y.values
if (debug):
    print y.head()
    print 'y.shape = ', y.shape
    print 'y_array.shape = ', y_array.shape
    print [col for col in y.columns if ('_GE' in col)]

#test-train-validation split is 1:1:1
train_fraction = 0.333
rn_seed = 14
from sklearn.model_selection import train_test_split
x_train, x_tv, y_train, y_tv = train_test_split(x_array, y_array, train_size=train_fraction, 
    test_size=(1-train_fraction), random_state=rn_seed)
train_fraction = 0.5
x_test, x_validate, y_test, y_validate = train_test_split(x_tv, y_tv, train_size=train_fraction,
    test_size=(1-train_fraction), random_state=rn_seed)
print x_array.shape, y_array.shape
print x_train.shape, y_train.shape
print x_test.shape, y_test.shape
print x_validate.shape, y_validate.shape

#plotting imports
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=1.5)

#build MLP classification model 
N_inputs = x.shape[1]
N_outputs = y.shape[1]
N_middle = N_inputs
layers = [N_inputs, N_middle, N_outputs]
dropout_fraction = 0.25
print 'layers = ', layers
print 'dropout_fraction = ', dropout_fraction
model = mlp_classifier(layers, dropout_fraction=dropout_fraction)
model.summary()

#fit model
N_epochs = 21
batch_size = 100
model = mlp_classifier(layers, dropout_fraction=dropout_fraction)
fit_history = model.fit(x_train, y_train, batch_size=batch_size, epochs=N_epochs, verbose=1, 
    validation_data=(x_validate, y_validate))

#plot loss vs training epoch
fig, ax = plt.subplots(1,1, figsize=(15, 6))
xp = fit_history.epoch#[1:]
yp = fit_history.history['loss']#[1:]
p = ax.plot(xp, yp, linewidth=1, label='training sample')
yp = fit_history.history['val_loss']#[1:]
p = ax.plot(xp, yp, linewidth=1, label='validation sample')
p = ax.set_title('loss function versus training epoch')
p = ax.set_ylabel('loss function')
p = ax.set_xlabel('training epoch')
p = ax.set_yscale('log')
p = ax.legend()
plt.savefig('figs/training_loss.png')
