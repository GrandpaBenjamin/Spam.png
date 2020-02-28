#Image Spam

from PIL import Image

img_num = 0
while True:
    img_num += 1
    img_name = str('Image Spam '+str(img_num))
    image_nam = Image.open('Spam.png.png')
    image_nam.show()
    print(f'file opened \'{img_name}\' ')
    
