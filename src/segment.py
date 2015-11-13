import numpy as np

from skimage import img_as_ubyte, transform, filters, morphology, exposure, io
from skimage.color.adapt_rgb import adapt_rgb, each_channel
from skimage.color import rgb2gray
from scipy import ndimage as ndi
import featextraction

import matplotlib.pyplot as plt


sobel = adapt_rgb(each_channel)(filters.sobel)


def segment(image, outfile):
    # Resize image: notice that x is height and y is width
    # 1. Reduce Canvas size based on prior info about this database
    h, w, c = image.shape
    x = round(0.15 * h)
    y = round(0.05 * w)  # x and y parameters are different from ISVC (.2,.1)
    h = h - x
    w = w - y
    cropped_pill = image[x:h, y:w]

    # 2. Reduce image size
    shrink_factor = 0.2
    w = round(cropped_pill.shape[0] * shrink_factor)
    h = round(cropped_pill.shape[1] * shrink_factor)
    small_pill= transform.resize(cropped_pill, (w, h))

    #3. Multiband sobel, combine channels and filter
    edges_pill = np.sum(sobel(small_pill), axis=2)
    edges_pill = exposure.rescale_intensity(edges_pill)

    smooth_pill = filters.rank.median(edges_pill, morphology.disk(3))

    bin_pill = (smooth_pill > smooth_pill.min())
    bin_pill = ndi.binary_fill_holes(bin_pill)
    plt.imsave(outfile, bin_pill, cmap='gray')

    #4. Calling feature extraction - TODO: put it in main
    filename=outfile.split('segmented.jpg')
    filenamefeat=filename[0]+'feat.csv'
    print(filenamefeat)
    featextraction.extract(rgb2gray(cropped_pill), bin_pill, filenamefeat)
