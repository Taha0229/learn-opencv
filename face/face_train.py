import cv2 as cv
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

train_dir = os.path.join("faces", "train")
val_dir = os.path.join("faces", "val")
haar_cascade = cv.CascadeClassifier('haar_face.xml')

train_datagen = ImageDataGenerator()
valid_datagen = ImageDataGenerator()

train_generator = train_datagen.flow_from_directory(train_dir, shuffle=False, class_mode='sparse', batch_size=1)
valid_generator = valid_datagen.flow_from_directory(val_dir, shuffle=False, class_mode='sparse', batch_size=1)

features = []
labels = []


data_size = len(train_generator)

for step in range(data_size):
    image, label = next(train_generator)    
    label = label.astype(int)[0]
    image = image.astype(np.uint8)[0]
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    for (x,y,w,h) in faces_rect:
        faces_roi = gray[y:y+h, x:x+w]
        features.append(faces_roi)
        labels.append(label)


features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)

print("labels: ", labels)