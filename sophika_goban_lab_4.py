# -*- coding: utf-8 -*-
"""
Automatically generated by Colab.

Create 30,000 samples, plot the initial dataset and incorporate shuffling dataset
"""

import numpy as np
import matplotlib.pyplot as plt

def get_dataset(shuffle):
  data=[]
  for i in range(30000):
    x_i= np.random.uniform(-1, 1)
    data.append([x_i, 0.2*x_i**4 + 2*x_i**3 + 0.1*x_i**2 + 10])

  data=np.array(data)

  plt.scatter(data[:, 0], data[:, 1])
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Initial plot of function")
  plt.grid()
  plt.show()

  if(shuffle==True):
    np.random.shuffle(data)

  return data

"""Splitting dataset into train, validation and test sets"""

def split_dataset(dataset, train_ratio, valid_ratio, test_ration):
  length= len(dataset)
  len_train= train_ratio*length
  len_valid= valid_ratio*length + len_train
  train=[]
  valid=[]
  test=[]
  for i in range(length):
    if(i < len_train):
      train.append(dataset[i])
    elif (i >= len_train and i < len_valid):
      valid.append(dataset[i])
    else:
      test.append(dataset[i])

  train= np.array(train)
  valid= np.array(valid)
  test= np.array(test)

  return train, valid, test

"""Scaling data from 0 to 1"""

def scale_data(dataset):
  data_x= dataset[:, 0]
  data_y= dataset[:, 1]

  scale_x= (data_x- np.min(data_x))/(np.max(data_x)-np.min(data_x))
  scale_y= (data_y- np.min(data_y))/(np.max(data_y)-np.min(data_y))

  scaled=[]
  for i in range(len(dataset)):
    scaled.append([scale_x[i], scale_y[i]])

  scaled= np.array(scaled)

  return scaled

"""Function to calculate the MAE, MSE, RMSE, and r2 score"""

from sklearn.metrics import r2_score

def get_Error(predicted, actual):
  m= len(actual)
  sum_mae=0
  sum_mse=0
  for i in range(m):
    sum_mae+=np.absolute(actual[i]-predicted[i])
    sum_mse+=np.square(actual[i]-predicted[i])

  MAE= sum_mae/m
  MSE= sum_mse/m

  RMSE= np.sqrt(MSE)

  score = r2_score(actual, predicted)

  return MAE, MSE, RMSE, score

"""Implementation- Shuffled"""

import tensorflow as tf

train_ratio= 0.3
valid_ratio= 0.2
test_ratio= 0.5

epoch_num= 20
batch_size= 12

dataset= get_dataset(True)
train, valid, test= split_dataset(dataset, train_ratio, valid_ratio, test_ratio)

"""Structure 1"""

def Execute_Model1(train, valid, test, epoch_num, batch_size, a):

  model= tf.keras.Sequential([
    tf.keras.layers.Dense(12, activation=a, input_shape=(1,)),
    tf.keras.layers.Dense(8, activation=a),
    tf.keras.layers.Dense(4, activation=a),
    tf.keras.layers.Dense(1)
  ])

  model.compile(optimizer='adam', loss='mean_squared_error')

  model.fit(train[:, 0], train[:, 1], epochs=epoch_num, batch_size=batch_size, validation_data=(valid[:, 0], valid[:, 1]), verbose=0)

  y_predict= model.predict(test[:, 0])

  MAE, MSE, RMSE, score= get_Error(y_predict, test[:, 1])

  print("MAE: ", MAE)
  print("MSE: ", MSE)
  print("RMSE: ", RMSE)
  print("r2_score: ", score)

  plt.scatter(test[:, 0], test[:, 1])
  plt.title("x_test vs. y_test")
  plt.xlabel("x_test")
  plt.ylabel("y_test")
  plt.grid()
  plt.show()

  plt.scatter(test[:, 0], y_predict)
  plt.title("x_test vs. y_predicted")
  plt.xlabel("x_test")
  plt.ylabel("y_predicted")
  plt.grid()
  plt.show()

"""Structure 2"""

def Execute_Model2(train, valid, test, epoch_num, batch_size, a):

  model= tf.keras.Sequential([
    tf.keras.layers.Dense(24, activation=a, input_shape=(1,)),
    tf.keras.layers.Dense(1)
  ])

  model.compile(optimizer='adam', loss='mean_squared_error')

  model.fit(train[:, 0], train[:, 1], epochs=epoch_num, batch_size=batch_size, validation_data=(valid[:, 0], valid[:, 1]), verbose=0)

  y_predict= model.predict(test[:, 0])

  MAE, MSE, RMSE, score= get_Error(y_predict, test[:, 1])

  print("MAE: ", MAE)
  print("MSE: ", MSE)
  print("RMSE: ", RMSE)
  print("r2_score: ", score)

  plt.scatter(test[:, 0], test[:, 1])
  plt.title("x_test vs. y_test")
  plt.xlabel("x_test")
  plt.ylabel("y_test")
  plt.grid()
  plt.show()

  plt.scatter(test[:, 0], y_predict)
  plt.title("x_test vs. y_predicted")
  plt.xlabel("x_test")
  plt.ylabel("y_predicted")
  plt.grid()
  plt.show()

"""Case 1"""

Execute_Model1(train, valid, test, epoch_num, batch_size, 'relu')

"""Case 2"""

Execute_Model2(train, valid, test, epoch_num, batch_size, 'relu')

"""Case 3"""

Execute_Model1(train, valid, test, epoch_num, batch_size, 'tanh')

"""Case 4"""

train_scale= scale_data(train)
valid_scale= scale_data(valid)
test_scale= scale_data(test)

Execute_Model1(train_scale, valid_scale, test_scale, epoch_num, batch_size, 'relu')

"""Case 5"""

Execute_Model1(train_scale, valid_scale, test_scale, epoch_num, batch_size, 'tanh')

"""Implementation- not shuffled

Case 1
"""

dataset= get_dataset(False)
train, valid, test= split_dataset(dataset, train_ratio, valid_ratio, test_ratio)
Execute_Model1(train, valid, test, epoch_num, batch_size, 'relu')

"""Case 2"""

Execute_Model2(train, valid, test, epoch_num, batch_size, 'relu')

"""Case 3"""

Execute_Model1(train, valid, test, epoch_num, batch_size, 'tanh')

"""Case 4"""

train_scale= scale_data(train)
valid_scale= scale_data(valid)
test_scale= scale_data(test)

Execute_Model1(train_scale, valid_scale, test_scale, epoch_num, batch_size, 'relu')

"""Case 5"""

Execute_Model1(train_scale, valid_scale, test_scale, epoch_num, batch_size, 'tanh')

"""It can be seen from above that shuffling, and scaling the data as well as using the tanh activation function and structure 1 provides the best accuracy in predictions.

Question 6

Assumptions:
- Number of layers: 1 hidden layer with 2 units, 1 input layer with 2 units and an output layer with 1 unit
- Activation Function: Sigmoid (Logistic Regression)
- Loss function: MSE
- Randomize the weights for the neural network
- Assume learning rate to be 0.75
- Assume number of epochs is 10000
- Assume batch size to be 1
- Assume that there is a bias node that will be randomized
- Assume that output that is >= 0.5 gets mapped to 1, else it gets mapped to 0
"""

import numpy as np

def sigmoid(x):
  y= 1/(1 + np.exp(-x))
  return y

def get_loss(predicted, actual):
  loss= 0.5 * (predicted - actual) ** 2
  return loss

import numpy as np

epoch_num= 10000
alpha= 0.75
batch_size= 1

#number of units in each layer
input_layer= 2
hidden_layer= 2
output_layer= 1

x_train= np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train= np.array([0, 1, 1, 0])

weights1 = np.random.randn(input_layer, hidden_layer) #input-hidden
bias1= np.random.randn(hidden_layer) #input_hidden
weights2= np.random.randn(hidden_layer, output_layer) #hidden-output
bias2= np.random.randn(output_layer)


for epoch in range(epoch_num):
  total_loss= 0
  predictions= []
  for i in range(len(x_train)):

    #Forward Propagation
    hidden_layer_input= np.dot(x_train[i], weights1) + bias1
    hidden_layer_output= sigmoid(hidden_layer_input)
    output_layer_input= np.dot(hidden_layer_output, weights2) + bias2
    output= sigmoid(output_layer_input)

    predictions.append(output)

    #Calculating loss
    total_loss += get_loss(output, y_train[i])

    # Backward Propagation
    output_error = output - y_train[i]
    output_delta = output_error * output * (1 - output)
    hidden_error = np.dot(weights2, output_delta)
    hidden_delta = hidden_error * hidden_layer_output * (1 - hidden_layer_output)

    #Update parameters
    weights2 -= alpha*np.outer(hidden_layer_output, output_delta)
    bias2 -= alpha*output_delta
    weights1 -= alpha*np.outer(x_train[i], hidden_delta)
    bias1 -= alpha*hidden_delta
  predictions= np.array(predictions)


for i in range(len(predictions)):
  if(predictions[i]>=0.5):
    predictions[i]= 1
  else:
    predictions[i]=0

print("Actual: ", y_train)
print("predicted: ", predictions)
