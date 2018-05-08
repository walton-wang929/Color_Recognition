# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 10:49:36 2017

@author: twang

color_recognization_v3

using opencv inrange function

"""

# import the necessary packages
import numpy as np
import cv2

def Color_Recognition_Range(image):
    '''
    '''
    image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#==============================================================================
#     # define color dictionary version1
#     dictionary ={'red':([17, 15, 100], [50, 56, 200]), 'blue':([100, 0, 0], [255, 50, 50]),
#                     'yellow':([0, 180, 180], [145, 255, 255]),'green':([50, 100, 0], [182, 255, 108]),
#                     'white':([240,240,240], [255, 255, 255]),'black':([0, 0, 0], [50, 50, 50]),
#                     'grey':([60,60,60], [200, 200, 200]),'purple':([40, 0, 80], [255, 110, 180]),}
#==============================================================================

#==============================================================================
#     # define color dictionary version2
#     dictionary ={'red':([42, 42, 165], [50, 50, 255]), 'blue':([180, 0, 0], [255, 50, 50]),
#                 'yellow':([0, 230, 230], [150, 255, 255]),'green':([0, 100, 0], [50, 255, 50]),
#                 'white':([240,240,240], [255, 255, 255]),'black':([0, 0, 0], [20, 20, 20]),
#                 'grey':([100,100,100], [130, 130, 130]),'purple':([80,0,80], [200,100,200]),
#                 'Maroon':([0,0,128], [50, 50, 150]),'Brown':([0, 0,150], [42,42,165]),
#                 'Cyan':([230,230,0], [255, 255, 120]),'Magenta':([200, 0,200], [255,100,255]),
#                 'Orange':([0,130,240], [100, 190, 255]),'Pink':([180, 170,230], [200,190,255]),
#                 'darkgray':([120,120,120], [180, 180, 180]),'Pinkh':([180, 170,230], [200,190,255]),
#                 }
#==============================================================================                     
       # define color dictionary version3
#==============================================================================
#     dictionary ={'red':([0, 0, 100], [80, 40, 255]), 'blue':([180, 0, 0], [255, 50, 50]),
#                 'yellow':([0, 230, 230], [150, 255, 255]),'green':([0, 100, 0], [50, 255, 50]),
#                 'white':([240,240,240], [255, 255, 255]),'black':([0, 0, 0], [20, 20, 20]),
#                 'grey':([100,100,100], [130, 130, 130]),'purple':([80,0,80], [200,100,200]),
#                 'Maroon':([0,0,128], [50, 50, 150]),'Brown':([0, 0,150], [42,42,165]),
#                 'Cyan':([230,230,0], [255, 255, 120]),'Magenta':([200, 0,200], [255,100,255]),
#                 'Orange':([0,130,240], [100, 190, 255]),'Pink':([180, 170,230], [200,190,255]),
#                 'darkgray':([120,120,120], [180, 180, 180]),'Pinkh':([180, 170,230], [200,190,255]),
#                     }
#==============================================================================
                    
#==============================================================================
#        # define color dictionary version4 HSV
#     dictionary ={
#                  'black':([0, 0, 0], [180, 255, 50]), 'blue':([88,70, 17], [112, 255, 255]),
#                 'orange':([0, 75, 0], [39, 255, 255]),'red':([112,131,130], [180,255,255]),
#                 'yellow':([20, 190, 20], [30, 255, 255]),'green':([57, 73, 0], [119, 255, 255]),
#                 'dark-red':([0, 107, 62], [6, 255, 255]),'Grey-blue':([88,70, 17], [112, 255, 255]),
#                 'White':([14, 0, 116], [180, 57, 255]),'Deep-purple':([18, 33, 6], [147, 159, 114]),
#                 'brown':([0, 64, 0], [21, 255, 255]),'Gray':([22, 0, 0], [180, 62, 255]),
#                 }
#==============================================================================

#==============================================================================
#     # define color dictionary version4 HSV
#     dictionary ={
#                  'black':([0, 0, 0], [179, 255, 50]), 'blue':([88,70, 17], [112, 255, 255]),
#                 'orange':([0, 75, 0], [39, 255, 255]),'red':([112,131,130], [180,255,255]),
#                 'yellow':([20, 190, 20], [30, 255, 255]),'green':([57, 73, 0], [119, 255, 255]),
#                 'dark-red':([0, 107, 62], [6, 255, 255]),'Grey-blue':([88,70, 17], [112, 255, 255]),
#                 'White':([14, 0, 116], [180, 57, 255]),'Deep-purple':([18, 33, 6], [147, 159, 114]),
#                 'brown':([0, 64, 0], [21, 255, 255]),'Gray':([22, 0, 0], [180, 62, 255]),
#                 'purple':([138, 120, 77], [155, 255, 255])       
#                 }  
#==============================================================================

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

#==============================================================================
# name = Color_Recognition_Range(image)
# cv2.putText(image,name,(10, 10), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
# cv2.imshow("images", image)
# cv2.waitKey(5000)
# 
# cv2.destroyAllWindows()    
#==============================================================================
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

print ("the dominant color is:", color)
