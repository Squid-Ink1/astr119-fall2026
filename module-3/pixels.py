# pixels_starter.py -- an image is an array (Pod 5). Copy this file to pixels.py and work on the copy.
# Run from the repository folder:  python module-3/pixels.py
import numpy as np
from matplotlib.pyplot import imread, imsave

I = imread("module-3/clean_io_small.png")     # rows, columns, 3 colour channels; values 0.0 to 1.0

J = I.copy()  # make a copy of the image array

n = 712
def fib(n):
    """Returns the Fibonacci sequence up to n.
    (I wanted to use the fibonacci sequence to generate a pattern for the image, but I didn't get that far.)"""
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

J[:, fib(n), :] = 0.0  # set a vertical line of pixels to black at column 349
J[fib(n), :, :] = 0.0  # set a line of pixels to black at Fibonacci indices

imsave("module-3/pixels_out.png", J)  # save the modified image

if __name__ == "__main__":
    print("shape:", I.shape)
    print(I.size)
    print(I[356,349])  # pixel at middle (row 356, column 349)
    print(I[0,0])  # pixel at top left
    print(fib(n))  # print the Fibonacci sequence up to n