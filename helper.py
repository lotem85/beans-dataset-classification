# count = 0
# fig = plt.figure(constrained_layout=True,figsize=(30,8))
# fig.suptitle('find the main leaf in image')
# subfigs = fig.subfigures(nrows=3, ncols=1)
# for row, subfig in enumerate(subfigs):
#     subfig.suptitle(labels_data[row])
#     nrows = leavsLimit // itemInRow
#     axs = subfig.subplots(nrows=nrows, ncols=itemInRow)
#     countRow = 0
#     for i, beanLeafImage in enumerate(onlyLeavsImages[count:count + leavsLimit]):
#         axs[countRow][i %itemInRow].imshow(beanLeafImage)
#         axs[countRow][i%itemInRow].axis('off')
#         if( (i+1) % itemInRow == 0) :
#             countRow +=1
#     count += leavsLimit
# Function to load and convert image to pixel data
import os
from PIL import Image
import numpy as np

def image_to_pixels(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure the image is in RGB mode
    img_array = np.array(img)  # Convert image to NumPy array
    img_array_flattened = img_array.flatten()  # Flatten the array
    return img_array_flattened.tolist()  # Convert flattened array to a list


def listImgDir(directory, imagesLimit = False):
    imagesPath = []
    if(imagesLimit) :
        filenames = os.listdir(directory)[:imagesLimit]
    else :
        filenames = os.listdir(directory)
    for filename in filenames:
        if filename.endswith('.jpg'): # Adjust file extensions as needed
             imagesPath.append(os.path.join(directory, filename))    
    return imagesPath    
