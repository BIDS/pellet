#featextraction
from skimage.measure import label, regionprops
import collections

def extract(imagegray, imagebin, outfile):
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

    #3. Save measurements for this pill
    od = collections.OrderedDict(sorted(all_props.items()))
    k = ", ".join(od.keys())
    v = ", ".join([str(f) for f in od.values()]) #notice you need to convert numbers to strings
    with open(outfile,'w') as f:
        #f.write(k)
        f.writelines([k,'\n',v])
