# -*- coding: utf-8 -*-
"""Oral_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tTHsGtNJaImRcqYGCM4fn3TvL3EB-ne6
"""

import tensorflow as tf
!pip install tensorflow ==<2.11.0>
print(tf.__version__)

from keras.preprocessing.image import ImageDataGenerator
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import glob as gb
#from keras.models import Sequential
from tensorflow.keras import layers, models
import cv2
import PIL
from tqdm import tqdm
from google.colab import drive
from google.colab.patches import cv2_imshow
from cv2 import *
import numpy as np
!pip install split-folders
import splitfolders
from splitfolders.split import ratio
#from keras import layers,datasets,models
from sklearn.model_selection import train_test_split
from sklearn import metrics
import os
import scipy
import  matplotlib.pyplot as plt
from google.colab import drive
from google.colab.patches import cv2_imshow
print(tf.__version__)

import sklearn
import skimage
from skimage.transform import resize
from sklearn.naive_bayes import GaussianNB
import glob
from sklearn import metrics
from sklearn.metrics import accuracy_score
from PIL import Image
import pandas as pd
#for saving model
import pickle
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from tensorflow import keras
from keras.layers import Dense,Conv2D,MaxPooling2D,Activation,Flatten,Dropout
#from keras.models import Sequential, load_model
from skimage.io import imread
import random
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array ,array_to_img
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import requests
import random

# reading and splitting data
#path="/content/drive/MyDrive/OralCancer_Last_data"
path="/content/drive/MyDrive/augmented_data"

splitfolders.ratio(path,"after_aug",(0.7,0.1,0.2))
# neww data more 800 image
# preprocessing 
# resize - re scale - normalization 
# 
# 1- data augmantation

def loadData(DataFolder):
  List_of_out=[]
  List_of_Img_names=[]
  binary_out=[]
  Images=[]
  for foldername in os.listdir(DataFolder):
    List_of_Img_names=os.listdir(str(DataFolder)+"/"+str(foldername))
    for image_name in range(len(List_of_Img_names)):
      image=cv2.imread(os.path.join(DataFolder,foldername,List_of_Img_names[image_name]))
      if image is not None:
        Image=cv2.resize(image,(50,50))
        Image=Image.astype("float32")/255.
        Images.append(Image)
        List_of_out.append(foldername)
  for item in List_of_out:
    if (item=='non_cancer'):
      binary_out.append(0)
    if(item=='cancer'):
      binary_out.append(1)
  Images=np.array(Images)
  #shuffle the data
  #Images=random.shuffle(Images)
  binary_out=np.array(binary_out)
  return Images,binary_out
X_train, Y_train = loadData("/content/after_aug/train")
X_test, Y_test = loadData("/content/after_aug/test")
X_val, Y_val = loadData("/content/after_aug/val")

from google.colab.patches import cv2_imshow
from cv2 import *
def GetDatasetSize(path):
    num_of_image = {}
    for folder in os.listdir(path):
        # Counting the Number of Files in the Folder
        num_of_image[folder] = len(os.listdir(os.path.join(path, folder)));
    return num_of_image;
    
path ="/content/drive/MyDrive/OralCancer_Last_data"
path2="/content/drive/MyDrive/augmented_data/"
DatasetSize = GetDatasetSize(path2);
print(DatasetSize);
#plt.imshow(X_train[0])
#plt.imshow(X_test[5])
#print(X_train[0])

# the model 
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(50,50, 3)))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(32, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Dropout(rate=0.25))
model.add(layers.Flatten())
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(8, activation='relu'))
model.add(layers.Dropout(rate=0.5))
model.add(Dense(2, activation='relu'))
model.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['accuracy'])
model.fit(X_train,Y_train,epochs=10,validation_data=(X_val,Y_val),batch_size=64)
y_pred = model.predict(X_test).argmax(axis=1)
print("Accuracy:  %.2f%%" % (metrics.accuracy_score(Y_test, y_pred)*100))

model.evaluate(x=X_test,y=Y_test)

#with open ("model5.h5","wb") as f:
#  pickle.dump(model,f)
#m4y_model= load_model("/content/drive/MyDrive/popppp/model8.h5")
#m4y_model.evaluate(x=X_test,y=Y_test)

print(tf.__version__)
model.save("/content/drive/MyDrive/popppp/model87.h5")

from keras import preprocessing
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import requests
import random
# data augmantation 
# Initialising the ImageDataGenerator class.
# We will pass in the augmentation parameters in the constructor.
datagen = ImageDataGenerator(
		rotation_range = 20,
		shear_range = 0.2,
		zoom_range = 0.2,
		horizontal_flip = True,
		brightness_range = (0.5, 1.5)
	)

def augmantation(DataFolder,save_path1,save_path2):
  List_of_out=[]
  List_of_Img_names=[]
  binary_out=[]
  Images=[]
  for foldername in os.listdir(DataFolder):
    List_of_Img_names=os.listdir(str(DataFolder)+"/"+str(foldername))
    for image_name in range(len(List_of_Img_names)):
      image= load_img(os.path.join(DataFolder,foldername,List_of_Img_names[image_name]))
      #image=cv2.imread(os.path.join(DataFolder,foldername,List_of_Img_names[image_name]))
      if image is not None:
        x = image
        List_of_out.append(foldername)

        # Converting the input sample image to an array
        # Reshaping the input image
        x=img_to_array(x)
        x = x.reshape((1, ) + x.shape)

        # Generating and saving 3 augmented samples
        # using the above defined parameters.
        i = 0
        for item in List_of_out:
          if (item=='non-cancer'):
            for batch in datagen.flow(x, batch_size = 1,
                        save_to_dir =save_path1,
                        save_prefix ='image', save_format ='jpg'):
              i += 1
              if i > 3:
                break
          if(item=='cancer'):
            for batch in datagen.flow(x, batch_size = 1,
                        save_to_dir =save_path2,
                        save_prefix ='image', save_format ='jpg'):
              i += 1
              if i > 3:
                break        
augmantation("/content/drive/MyDrive/OralCancer_Last_data","/content/drive/MyDrive/augmented_data/non_cancer","/content/drive/MyDrive/augmented_data/cancer")



#def Augmantation (Image,Folder_path):
# Loading a sample image
image=cv2.imread("/content/drive/MyDrive/OralCancer_Last_data/non-cancer/12654650-6954555-image-a-22_1556101508834-Edited.jpg")
#img = load_img('')
print(img)
# Converting the input sample image to an array
x = img_to_array(img)
print(x)

# Reshaping the input image
x = x.reshape((1, ) + x.shape)

# Generating and saving 5 augmented samples
# using the above defined parameters.
i = 0
for batch in datagen.flow(x, batch_size = 1,
						save_to_dir ='/content/ff',
						save_prefix ='image', save_format ='jpeg'):
	i += 1
	if i > 5:
		break

from google.colab import drive
drive.mount('/content/drive')

!pip show tensorflow