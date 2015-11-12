#featextraction
from skimage.measure import label, regionprops

def segment(imagegray, imagebin, outfile):
    # Resize image: notice that x is height and y is width
    # 1. Reduce Canvas size based on prior info about this database

    # 2. Reduce image size
    #Remove whatever is not a scalar or list

    regions = regionprops(imagebin,imagegray) #notice that you need to also
    all_props = {p:regions[0][p] for p in regions[0] if p not in ('image','convex_image','filled_image')}

    for p, v in list(all_props.items()):
        if isinstance(v,np.ndarray):
            if(len(v.shape)>1):
                del all_props[p]

    for p, v in list(all_props.items()):
        try:
            L = len(v)
        except:
            L = 1
        if L>1:
            del all_props[p]
            for n,entry in enumerate(v):
                all_props[p + str(n)] = entry
