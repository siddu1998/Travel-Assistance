import sys
from PIL import Image
import os
import glob

file_open = lambda x,y: glob.glob(os.path.join(x,y))
image_dir1 = "C:/Users/msais/Desktop/GTechSummer/images"
images = file_open(image_dir1,"*.ppm")

for image in images:
    im = Image.open("{}".format(image))
    im.save("{}.jpeg".format(image[-9:-4]))
    