# Image File Converter:

This program converts images from one file type to another using the Pillow Python Imaging Library. It can be especially useful to convert a large amount of images with minimal effort. It currently converts to BMP, JPEG, DDS, DIB, EPS, GIF, PNG and PDF files. It however does not convert from PDF files. 

# Requirments 
Before downloading and using the program, ensure that you have all the images you would like to convert in one folder. Ensure you have python3, along with the sys, os, and pillow modules installed.

# Usage
After installing python3 and the required modules (see Requirments above). Open the terminal. You can open directories using ```cd 'directory'``` and view which files are in the directory using ```ls```. 
Now perform a git clone:
``` 
git clone https://github.com/bdakhel/Image-File-Converter.git
```
Now go to your files and move the folder of images into your Image-File-Converter folder (should now contain Fileconverter.py, README.md and folder of files you would like to convert.
Head to terminal and open the Image-File-Converter folder. You can open directories using ```cd 'directory'``` and view which files are in the directory using ```ls```.
Type into terminal:
```python3 'input_directory/' 'output_directory' 'new_filetype' ```
Where 'input_directory/' is the name of your folder ending with a '/', 'output_directory' is what you would like your folder of new images to be named ending with w '/' and 'new_filetype' is the code for the new file type such as: BMP, JPEG, DDS, DIB, EPS, GIF, PNG and PDF.
Now you should have a new folder with the name you assigned it containing the converted images.
