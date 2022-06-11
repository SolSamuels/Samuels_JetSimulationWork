#!/usr/bin/env python
# coding: utf-8

# Program Name: Jetstarterprogram.py
# 
# Date: 6/11/2022
# 
# Creator: Sol Samuels
# 
# Description: 
#  - This program is a method tester program for the program Jet_Length_Width_Determiner_v1.py
#  - Not streamlined as intended.
# 

# In[1]:


import astropy.io
import numpy as np
import os
import glob
import matplotlib.pyplot as plt

from astropy.io import fits


# In[2]:


path = '**/Group*0.00_1.00_0.00*.fits*'
print(glob.glob(path, recursive=True))
for file in glob.glob(path, recursive=True):
    print(file)


# In[3]:


#Opens and displays list of FITS file Extension HDUs

fits_image_hdul = fits.open('Group_L446_rc30_beta07_0040_nu=30.0_los=0.00_1.00_0.00_4.0Myr.fits.gz')
fits_image_hdul.info()


# In[4]:


#Displays FITS Image title, time index, and pixel size

sim_title = fits_image_hdul[0].header['OBJECT']
sim_time = fits_image_hdul[0].header['TIME']
pixel = fits_image_hdul[0].header['CDELT1']

print(sim_title)
print("Time index: {}".format(sim_time))
print("Pixel size: {}".format(pixel))


# In[5]:


#Displays Entire FITS Image Header

hdr = fits_image_hdul[0].header
header = repr(hdr)
print(header)


# In[6]:


#Difines Data From FITS image and records image dimensions

data =  fits_image_hdul[0].data
print(data)

length = len(data[0])
print(length)

width = len(data)
print(width)


# ## DETERMINING LENGTH

# In[7]:


#Creates list of slice sums

slice_vals = []

for row in data:
    slice_sum = 0
    for element in row:
        slice_sum += element
    slice_vals.append(slice_sum)
    
print(slice_vals)


# In[8]:


#Creates list of Cumultive Sum values

cul_vals = []
movingsum = 0

for element in slice_vals:
    movingsum += element
    cul_vals.append(movingsum)
    
print(cul_vals)


# In[9]:


plt.hist(slice_vals)
plt.show()


# In[10]:


y_val = []
for x in range(length):
    y_val.append(x)
    
print(len(y_val))


# In[11]:


plt.bar(y_val, cul_vals)
plt.show()


# In[12]:


max_val = cul_vals[-1]
norm_cul_vals = []
norm = 0

for element in cul_vals:
    norm = element / max_val
    norm_cul_vals.append(norm)
    
print(norm_cul_vals)
    


# In[13]:


plt.bar(y_val, norm_cul_vals)
plt.xlabel("Image y-value")
plt.ylabel("Normalized Cumulative Value")
plt.show()


# In[14]:


norm_cul_vals_edit = []
prev_ele = 0

for element in norm_cul_vals:
    if element != 0 and element != prev_ele:
        norm_cul_vals_edit.append(element)
    prev_ele = element
        
print(norm_cul_vals_edit)

y_vals = []
for x in range(len(norm_cul_vals_edit)):
    y_vals.append(x)


# In[15]:


plt.bar(y_vals, norm_cul_vals_edit)
plt.xlabel("Number of pixels from bottom edge of jet")
plt.ylabel("Normalized Cumulative Value")
plt.show()


# In[16]:


pixel_count = 0
for element in norm_cul_vals_edit:
    if element <= 0.98:
        pixel_count += 1
        
print("Length of Jet in Pixels: {} pixels".format(pixel_count))


# In[17]:



pixel_size = float(pixel[:-3])

jet_size_y = pixel_size * pixel_count
print("Jet Length (in y direction): {} cm".format(jet_size_y))


# ## DETERMINING WIDTH

# In[18]:


data_reorient = []

for x in range(width):
    col_sub = []
    for row in data:
        col_sub.append(row[x])
    data_reorient.append(col_sub)
    
    


# In[19]:


col_slice_vals = []

for row in data_reorient:
    slice_sum = 0
    for element in row:
        slice_sum += element
    col_slice_vals.append(slice_sum)
    
print(col_slice_vals)


# In[20]:


col_cul_vals = []
movingsum = 0

for element in col_slice_vals:
    movingsum += element
    col_cul_vals.append(movingsum)
    
print(col_cul_vals)


# In[21]:


max_val = col_cul_vals[-1]
norm_cul_vals = []
norm = 0

for element in col_cul_vals:
    norm = element / max_val
    norm_cul_vals.append(norm)
    
print(norm_cul_vals)
    


# In[22]:


norm_cul_vals_edit = []
prev_ele = 0

for element in norm_cul_vals:
    if element != 0 and element != prev_ele:
        norm_cul_vals_edit.append(element)
    prev_ele = element
        
print(norm_cul_vals_edit)

x_vals = []
for y in range(len(norm_cul_vals_edit)):
    x_vals.append(y)
    
print(x_vals)


# In[23]:


plt.bar(x_vals, norm_cul_vals_edit)
plt.xlabel("Number of pixels from left edge of jet")
plt.ylabel("Normalized Cumulative Value")
plt.show()


# In[24]:


pixel_count = 0
for element in norm_cul_vals_edit:
    if element <= 0.98:
        pixel_count += 1
        
print("Width of Jet in Pixels: {} pixels".format(pixel_count))

pixel_size = float(pixel[:-3])

jet_size_y = pixel_size * pixel_count
print("Jet Width (in x direction): {} cm".format(jet_size_y))


# In[ ]:




