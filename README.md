# InteractiveImageSegmentation
An interactive image segmentation tool for pixel-wise labeling image dataset in segmentation task, 
which use GrabCut("[“GrabCut”: interactive foreground extraction using iterated graph cuts](https://dl.acm.org/citation.cfm?id=1015720)") and implemented in OpenCV 3 and Python.
An OpenCV tutorial can be found [here](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_grabcut/py_grabcut.html?highlight=grabcut).

## Quick Start
Go to this project dir and run 'python interactive_image_segmentation.py resouce/images/ resouce/labels'. You will see a UI window and you can start labelling.
If you want to label your own images, collect them into a filefolder, modify the source_dir and save_dir.

## How to use
- CTRL+left mouse button: label certain background pixels
- SHIFT+left mouse button: label certain foreground pixels
- CTRL+right mouse button: label possible background pixels
- SHIFT+right mouse button: label possible foreground pixels
- 'a'/SPACE: run sengementation again
- 's'/ENTER: save label and skip to next image
- 'p': prev image
- 'n': next image
- 'q'/ESC: exit

There are some useful py scripts you can use to handle your own data. Usage:
- 'interactive_image_segmentation.py image_dir save_dir' runs interactive image segmentation
- 'batch_rename.py dir1 [dir2] ...' renames all images in folder with sequencial numbers.
- 'img_cvt_format.py image_dir [suffix]' converts all images in folder to the same image format, such as '.png' '.jpg'...
- 'video2img.py video_file save_dir [stride] [resize] [suffix]' converts a video file to a list of images.