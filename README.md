# thumbnails
Simple python thumbnailer

Given a directory full of images it uses pillow to generate a 'medium' and 'thumbnail' version of all the jpegs it finds. It will not overwrite existing images and can be run many times on the same directory.

Simply 'pip install pillow', change the directory to your image location, and run from the command line.

I save all my images with no suffix (just chinatown01.jpg for example), and I save details with the \_det suffix, (chinatown01_det01.jpg). This script ignores any image with \_det for that reason. It appends it's own suffix for thumbnails and medium sized images, which you can change. It will also ignore those (so it doesn't make thumbnails of thumbnails).

