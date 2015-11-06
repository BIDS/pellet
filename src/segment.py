import joblib
import os
from os.path import join as pjoin



def _segment_image(image_collection, n, target):
    fname, ext = os.path.splitext(image_collection.files[n])
    fname = os.path.basename(fname)
    outfile = pjoin(target, fname + '_segmented' + ext)

    if os.path.exists(outfile):
        return
    else:
        print('Segmenting {}'.format(outfile))


def segment(image_collection, target):
    """Segment all images in the specified collection.

    Parameters
    ----------
    image_collection : ImageCollection
        Input images.
    target : str
        Output directory.

    """
    res = joblib.Parallel(n_jobs=4, verbose=5)(
        joblib.delayed(_segment_image)(image_collection, nr, target)
        for nr in range(len(image_collection)))
