import PIL
from PIL import Image
from tkinter.filedialog import *

imgpath= askopenfilename()
img= PIL.Image.open(imgpath)
myHeight, myWidth = img.size

#compression

img=img.resize((myHeight, myWidth), PIL.Image.ANTIALIAS)
savepath= asksaveasfilename()

#image_conversion
img= img.convert('RGB')

#saving_image
img.save(savepath+"compressed.jpg")
