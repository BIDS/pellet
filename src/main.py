import os
from os.path import join as pjoin

import data
import segment
import parallel


base = os.path.dirname(__file__)
output = pjoin(base, '../output')

if not os.path.isdir(output):
    print('Creating output directory...')
    os.mkdir(output)
    os.mkdir(pjoin(output, 'segmented'))


images = data.load('dr')
parallel.apply_parallel(images, segment.segment,
                        output_dir=output, postfix='segmented')
