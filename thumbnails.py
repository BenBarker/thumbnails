'''
Create small and thumbnail versions of images in directory.
Does not overwrite existing images.
Skips images that are already named like small or thumbnail images.

Uses pillow, python 3.4
'''
import os
from PIL import Image

#Set to False to only print rather than actually save
save = True 

#change to your image location
imageDirectory = '/Users/ben/Google Drive/Art/image_db'  

thumbSuffix = '_tn'
smallSuffix = '_sm'
detailSuffix = '_det'
smallSize = 1000
thumbSize = 128


def makeSizes(imagePath):
    '''generate a thumbnail and small from the given image path'''

    #check input and deconstruct
    if not os.path.exists(imagePath):
        print('cannot find image, skipping:',imagePath)
        return
    if not imagePath.lower().endswith('.jpg'):
        print('image must end with .jpg')
        return
    pathName,fileName = os.path.split(imagePath)
    base,ext = os.path.splitext(fileName)

    im = Image.open(imagePath)

    #Do 'small' version
    smallName = base+smallSuffix+ext
    smallPath = os.path.join(pathName,smallName)
    if os.path.exists(smallPath):
        #print('small already exists, skipping',smallName)
        pass
    else:
        im.thumbnail((smallSize,smallSize))
        print('*'*5,'saving',smallPath,'*'*5)
        if save:
            im.save(smallPath,'JPEG',quality=80)

    #Do thumbnail
    thumbName = base+thumbSuffix+ext
    thumbPath = os.path.join(pathName,thumbName)
    if os.path.exists(thumbPath):
        #print('thumbnail already exists, skipping',thumbName)
        pass
    else:
        im.thumbnail((thumbSize,thumbSize))
        print('*'*5,'saving',thumbPath,'*'*5,)
        if save:
            im.save(thumbPath,'JPEG')


#main
for dirpath, dnames, fnames in os.walk(imageDirectory):
    for f in fnames:
        #skip details, thumbs, and smalls
        if (detailSuffix in f) or (smallSuffix in f) or (thumbSuffix in f):
            continue
        #skip non jpgs
        if not f.lower().endswith('.jpg'):
            continue

        full_path = os.path.join(dirpath, f)
        makeSizes(full_path)