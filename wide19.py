
from PIL import Image

inputImage = input("Insert Image Here: ")
resizeval = input("Resize value: ")
image1 = Image.open(inputImage)
oldsize = list(image1.size)
width = int(oldsize[0])
oldheight = int(oldsize[1]) 
height = oldheight * int(resizeval)
print(width, oldheight, resizeval)
newsize = (int(height), int(width))
new_image = image1.resize(newsize)
rgb_im = new_image.convert('RGB')
rgb_im.save("output.jpg")