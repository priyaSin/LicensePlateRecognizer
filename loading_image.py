
# coding: utf-8

# # Step 1 : Loading and thresholding a car's image

# In[19]:

from skimage.io import imread
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt
import cv2


# In[20]:

#Loading the car image in grey scale
car = imread("car.jpg" , as_grey = True)
print(car)


# In[21]:

#The above values are floats between 0 and 1, gray scale
#We will convert it into 0 to 255 for the sake of making visualisation easier.  
#You can skip this step
car = car * 255
#Visualising the change
plt.imshow(car ,                                 #Giving car image
                cmap = "gray")             # setting cmap value
plt.show() 


# In[22]:

#Making a histogram of the above image to see if it is a bimodal image
#OTSU_BINARIZATION - An algo which calculates threshols value works best for bimodal image

#hist = cv2.calcHist([car])
plt.hist(car)
plt.show()

#We can see that it is bimodal image so we can use otsu binarization for thresholding


# In[23]:

#Right now we have 256 shades in the present image and we want to 
#convert the image in black or white pixel value only
#Hence, we will set a threshold value and accordingly for pixel 
#value greater than threshold value are set to 255 and less than threshold value are given 0

print("Image array before thresholding:")
print(car)


threshold_value = threshold_otsu(car) #
car = car > threshold_value

print("Image array after thresholding:")
print(car)

print("Car Binary image")
plt.imshow(car , cmap = "gray")
plt.show()


# In[ ]:




# In[ ]:



