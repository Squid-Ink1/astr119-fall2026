# pixels_starter.py -- an image is an array (Pod 5). Copy this file to pixels.py and work on the copy.
# Run from the repository folder:  python module-3/pixels.py
import numpy as np
from matplotlib.pyplot import imread, imsave

I = imread("module-3/clean_io_small.png")     # rows, columns, 3 colour channels; values 0.0 to 1.0

J = I.copy()  # make a copy of the image array
J[20:40, 20:40, :] = 1.0  # set a square of pixels to white
J[356, :, :] = 0.0  # set a line of pixels to black
imsave("module-3/pixels_out.png", J)  # save the modified image

if __name__ == "__main__":
    print("shape:", I.shape)
    print(I.size)
    print(I[356,349])  # pixel at middle (row 356, column 349)
    print(I[0,0])  # pixel at top left
