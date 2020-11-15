# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 00:44:24 2020

@author: mohin
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:47:06 2020

@author: mohin
"""

from PIL import Image,ImageChops
import numpy as np

im = Image.open("original.png")
im2=Image.open("download.png")

diff= ImageChops.difference(im,im2)
print(diff.getbbox())
diff.show()