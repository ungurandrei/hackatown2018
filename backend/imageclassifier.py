import numpy as np
from keras.models import Sequential
from keras.models import load_model
import cv2

# Load keras image classification Conv. Neural Net
model = load_model('../number_model.h5')


# For now, basic image classification test with MNIST data
def classify_image_test():
    img = cv2.imread('test_img4.png')
    img = cv2.bitwise_not(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (28, 28))
    print(img.shape)
    
    k = np.array(img)
    y= k.reshape(1,28,28,1)

    prediction = model.predict_classes(y)[0]
    return prediction

#The real function we will use: the image will come from our front end
def classify_image(img):
    img = cv2.bitwise_not(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (28, 28))
    print(img.shape)
    
    k = np.array(img)
    y= k.reshape(1,28,28,1)

    prediction = model.predict_classes(y)[0]
    return prediction