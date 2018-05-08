# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:11:33 2017

@author: TWang

color recognition:
    
update: add kmeans to segmentation clothes and body 

then using range for color recognition

"""
# import the necessary packages
import numpy as np
import cv2

def Color_Recognition_Range(image):
    '''
    '''
    image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    dictionary ={
                    'White':([0, 0, 116], [180, 57, 255]),
    
                    'Light-red':([0,38, 56], [10,255,255]),
                    'orange':([10, 38, 71], [20, 255, 255]),
                    'yellow':([18, 28, 20], [33, 255, 255]),
                    'green':([36, 10, 33], [88, 255, 255]), 
                    'blue':([87,32, 17], [120, 255, 255]),
                    'purple':([138, 66, 39], [155, 255, 255]),
                    'Deep-red':([170,112, 45], [180,255,255]),
    
                    'black':([0, 0, 0], [179, 255, 50]),      
                    }  
    
    color_name = []
    color_count =[]
             
    # loop over the boundaries
    for key,(lower,upper) in dictionary.items():
        
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")
         
        # find the colors within the specified boundaries and apply
        # the mask
     
        mask = cv2.inRange(image_HSV, lower, upper)
        
        cv2.imshow("mask", mask)
        cv2.waitKey(1000) 
        cv2.destroyAllWindows()
         
        count = cv2.countNonZero(mask)
        
        color_count.append(count)
        
        color_name.append(key)
    
    color_count_array = np.array(color_count)
    
    idx = np.argmax(color_count_array)

    color = color_name[idx]
    
    return color
    
      
# load the image
image = cv2.imread('test.jpg')

image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 

dictionary ={
                    'White':([0, 0, 146], [180, 34, 255]),
                    'Gray':([0, 0, 22], [180, 34, 146]),
                    'Light-red':([0,157, 25], [6,255,255]),
                    'Light-Pink':([0,0, 25], [6,157,255]),
                    'Orange':([6, 33, 168], [23, 255, 255]),
                    'Brown':([6, 33, 25], [23, 255, 168]),
                    'yellow':([23, 33, 25], [32, 255, 255]),
                    'Green':([32, 33, 25], [75, 255, 255]), 
                    'Blue-Green':([75, 33, 25], [90, 255, 255]), 
                    'Blue':([90,33, 45], [123, 255, 255]),
                    'Purple':([123, 112, 25], [155, 255, 255]),
                    'Light-Purple':([123, 33, 25], [155, 125, 255]),                   
                    'Pink':([155,34, 25], [180,225,255]),
                    'Deep-Pink':([175,0, 25], [180,157,255]),
                    'Deep-red':([175,157, 25], [180,255,255]),    
                    'black':([0, 0, 0], [180, 255, 26]),      
                    }  
    
color_name = []
color_count =[]
             
# loop over the boundaries
for key,(lower,upper) in dictionary.items():
    
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
     
    # find the colors within the specified boundaries and apply
    # the mask
    
    print(key)
 
    mask = cv2.inRange(image_HSV, lower, upper)
    
    cv2.imshow("mask", mask)
    cv2.waitKey(1000) 
    cv2.destroyAllWindows()
     
    count = cv2.countNonZero(mask)
    
    color_count.append(count)
    
    color_name.append(key)
        
    
color_count_array = np.array(color_count)

idx = np.argmax(color_count_array)

color = color_name[idx]

print ("dominant color:", color)
