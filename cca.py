
# coding: utf-8

# # Number Plate Extraction from the loaded image using Connected Component Analysis
# 
# #### Other techniques of detection can also be used

# In[1]:

from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import loading_image


# In[82]:

#Now we are going to label the loaded image. Labelling here means
#measuring all the small connected components or small regions in an image

label_img = measure.label(loading_image.car)

#Dsiplaying the labelled image components
fig, ax1 = plt.subplots(1)


# In[83]:

#Seeing how the array looks like (You can skip this)

print(label_img[5 , :])
# as the array is large only seeing 5 row, else wont be able to analyze
#So labelling basically happens by giving a regions of pixels same value


# In[85]:

# Regions have been created.
# There are various properties related to a region.
# For example, region area - Number of pixels in the region
# bounding box of a region - (min_row, min_col, max_row, max_col)
# Centroid - gives the coordinates of centroid of the region


min_height , max_height , min_width , max_width = (0.02 * label_img.shape[0] , 0.2* label_img.shape[0] , 0.08* label_img.shape[1] , 0.40*label_img.shape[1]) 

license_plate_img = []         #Explained later
license_plate_coordinates = []

# We loop through each region and check if it might be a license plate region
# if we suspect it to be the same we will draw a rectangle around it to highlight
#print((regionprops( label_img )))
for region in regionprops( label_img ):
    if region.area < 1500:
        #eliminating all the regions which are too small to be considered for license plate
        continue
    print(region.area)  
    #Else get the bounding box coordinates of the region and draw a rectangle over it
    min_row , min_col , max_row , max_col = region.bbox
    
    width = max_col - min_col
    height = max_row - min_row
    
    # A few characterstics of a nuel_imgmber plate are:
    # 1. Rectangular in shape
    # 2. Width is more than the height
    # 3. proportion of the width of LP region to full image ranges between 10% to 40%
    # 4. Simiraly height proportion ranges from 8% to 20%
    
    #Based on the above criteria, we will find possible regions
    if height >= min_height and height <= max_height and width >= min_width and width <= max_width and width > height:
        
        #Take the regions in a list which are possibly be regions of lincense plate and coordinates also
        license_plate_img.append(loading_image.car[min_row : max_row , min_col : max_col])
        license_plate_coordinates.append((min_row , min_col , max_row , max_col))
        
        
        #Draw a rectangle with lower left at xy = (x, y) with specified width, height and rotation angle.
        patch = patches.Rectangle((min_col , min_row) , width , height , edgecolor = "cyan" , linewidth = 2 , fill = False)        
        ax1.add_patch(patch)
    
ax1.imshow(label_img , cmap = "gray")   
plt.show()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



