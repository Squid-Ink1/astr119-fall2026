#------------------------------------------------------------------------------
# pixelfixer.py: a command-line utility that fixes red-corrupted pixels in an
# RGB image.
#
# Run with:
#   python pixelfixer.py easy_corrupt_io_small.png
# which writes fixed_easy_corrupt_io_small.png next to the input.
#------------------------------------------------------------------------------
import sys
import numpy as np
from matplotlib.pyplot import imread, imsave

def corruptcount(I):
    """Step 1: Find the bad pixels and print how many"""
    
    count = 0
    for m in range(1, I.shape[0]-1):
        for n in range(1, I.shape[1]-1):
            if I[m, n, 0] == 1 and I[m, n, 1] == 0 and I[m, n, 2] == 0:  # Checks if a pixel is "bad" on the original image
                count = count + 1   # Increases the bad pixel count
    return count

def pixelfix(I):
    """Replace bad pixels with the color averaged from their neighbors.

    Parameters
    ----------
    I : ndarray, shape (M, N, 3)
        A color image array in RGB format, values between 0 and 1.
        A bad pixel has red = 1, green = 0, blue = 0.

    Returns
    -------
    Iq : ndarray, same shape as I
        A copy of the image with the bad pixels fixed.
    """
    Iq = I.copy()

    for m in range(1, Iq.shape[0]-1):
            for n in range(1, Iq.shape[1]-1):
                if Iq[m, n, 0] == 1 and Iq[m, n, 1] == 0 and Iq[m, n, 2] == 0:  # Checks if a pixel is "bad" on the copied image

                    """Step 2: Set the corrupted pixels to white (obsolete with step 3, but here it is)"""
                    Iq[m, n, :] = 1

                    """Step 3: """
                    upr = Iq[m-1, n, 0]
                    downr = Iq[m+1, n, 0]
                    rightr = Iq[m, n+1, 0]
                    leftr = Iq[m, n-1, 0]
                    # Finds the red values of the four neighboring pixels

                    upg = Iq[m-1, n, 1]
                    downg = Iq[m+1, n, 1]
                    rightg = Iq[m, n+1, 1]
                    leftg = Iq[m, n-1, 1]
                    # Finds the green values of the four neighboring pixels

                    upb = Iq[m-1, n, 2]
                    downb = Iq[m+1, n, 2]
                    rightb = Iq[m, n+1, 2]
                    leftb = Iq[m, n-1, 2]
                    # Finds the blue values of the four neighboring pixels

                    redavg = (upr + downr + rightr + leftr) / 4 # Finds the average red value
                    greenavg = (upg + downg + rightg + leftg) / 4   # Finds the average green value
                    blueavg = (upb + downb + rightb + leftb) / 4    # Finds the average blue value
                    
                    Iq[m, n, 0] = redavg
                    Iq[m, n, 1] = greenavg
                    Iq[m, n, 2] = blueavg



   
    ### YOUR WORK GOES HERE (with the agent, under the Protocol, in stages:
    ### 1. find the bad pixels and print how many;
    ### 2. paint them white and look at the result;
    ### 3. replace the white with the average of the up/down/left/right
    ###    neighbors. Then try solo_corrupt_io_small.png.)

    return Iq

def _main():
    image_file = sys.argv[1]
    I = imread(image_file)

    print(f"There are {corruptcount(I)} corrupted pixels in the original image")    # Prints the count of corrupted pixels before any are restored

    I = pixelfix(I)
    imsave('fixed_' + image_file, I)
    print(f"Wrote fixed_{image_file}")


if __name__ == '__main__':
    _main()
