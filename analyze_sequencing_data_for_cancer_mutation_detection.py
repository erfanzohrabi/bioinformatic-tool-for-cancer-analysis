"""Developing a Python program to analyze high-throughput sequencing data for cancer mutation detection"""

#import necessary libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report


#load the data and clean it 
data = pd.read_csv('sequencingData.csv')  #load the data 
data = data.dropna() #drop any rows with missing values 
data = data[data['mutation'] != 'Wildtype'] #remove wildtype samples from dataset 

#separate features and labels 
X = data.iloc[:,:-1] #features 
y = data['mutation'] #labels

#scale the features using standard scaler 
scaler = StandardScaler()   #instantiate scaler object 
X = scaler.fit_transform(X) #scale the features

#split into training and testing sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#build logistic regression model and fit to training set  
model = LogisticRegression()   #instantiate model object 
model.fit(X_train, y_train)    #fit model to training set
  
#make predictions on test set                                                                     
y_preds = model.predict(X_test)

#evaluate model performance on test set using confusion matrix, accuracy score and 
#classification report                                                                                                                                                                                                                                                                                                                                                                         
                                             
                                        
                                           
print('Confusion Matrix: \n', confusionMatrix(yTest, yPreds))                         
print('Accuracy Score: \n', accuracyScore(yTest, yPreds))                         
print('Classification Report: \n', classificationReport(yTest, yPreds))