import sys
from PIL import Image
import caffe
import numpy as np
import pandas as pd

import itertools
from scipy.stats import pearsonr

def evaPearsonr(gt, pred):
    return pearsonr(gt, pred)

def getGT(gt_file):
    gt = []
    images = []
    for line in open(gt_file, 'r'):
        fle, rating = line.strip().split()
        gt.append(float(rating))
        images.append(fle)
    return gt, images

def infe():
    net = caffe.Net('webthetics.prototxt','./model/webthetics.caffemodel', caffe.TEST)
    net.forward()
    rating = net.blobs['fc8'].data
    loss = net.blobs['loss'].data

    batch_size = 98 # It should be same as webthetics.prototxt (e.g. `batch_size: 98`)
    gt_file = './data/baconbao-predict.txt' # It should be same as webthetics.prototxt
    gt, images = getGT(gt_file)
    irr_rating = list(itertools.chain.from_iterable(rating))
    res = np.array(irr_rating)

    # Check of batch size setting
    if (len(images) > len(irr_rating)):
        raise Exception("[BaconBao] Error: Batch size should be large than length of predict images")

    # Prepare the shape of dataframe
    n = len(images)
    m = (batch_size//len(images))
    if (batch_size%len(images) != 0):
        m = (batch_size//len(images)) + 1
    
    # Pad NaN to the end
    res = np.pad(res.astype(float), (0, m*n - res.size), mode='constant', constant_values=np.nan).reshape(m,n)

    # Show results
    res_df = pd.DataFrame(res, columns=images)
    print(res_df)
    print(res_df.describe())
    print('------------')
    for img in images:
        print(img, round(res_df[img].mean(), 5))

if __name__ == '__main__':
    try:
        infe()
    except KeyboardInterrupt:
        sys.exit(0)
