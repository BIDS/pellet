import os
from os.path import join as pjoin
import warnings

import data
import segment
import parallel


base = os.path.dirname(__file__)
output = pjoin(base, '../output')

outputs = {'output': output, 'segmentation': pjoin(output, 'segmented')}

for folder in outputs.values():
    if not os.path.isdir(folder):
        print('Creating {}'.format(folder))
        os.mkdir(folder)

images = data.load('dr')

with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=UserWarning)

    parallel.apply_parallel(images, segment.segment,
                            output_dir=outputs['segmentation'],
                            postfix='segmented')
