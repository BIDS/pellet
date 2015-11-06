from skimage import io
import os

data_dir = os.path.join(os.path.dirname(__file__), '../data/pir-challenge')


def load(subset):
    if subset.lower() == 'dr':
        return io.imread_collection(os.path.join(data_dir, 'dr/*'))
