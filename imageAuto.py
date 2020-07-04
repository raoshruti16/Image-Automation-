# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 17:30:04 2020

@author: shruti
"""

from PIL import Image
import os

for i in os.listdir('C:\image_automation'): #listing each item in a folder
    files = os.listdir('C:\image_automation/%s'%i)
    for j in files:
        img = Image.open('C:\image_automation/%s/%s'%(i,j)) # image extension *.png,*.jpg
        new_width  = 200
        new_height = 300
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save('C:\image_automation\%s_%s.png'%(i,j)) # format may what u want ,*.png,*jpg,*.gif