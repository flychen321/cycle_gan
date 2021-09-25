import glob
import os
import shutil

import cv2
import numpy as np

# image size: 128 * 64 *3
# select_mode = 'm2d'
select_mode = 'd2m'
src_path = 'results/market/bounding_box_train_camstyle'
dst_path = 'results/market/bounding_box_train_' + select_mode
files = glob.glob(src_path+'/*.jpg')
if os.path.exists(dst_path):
    shutil.rmtree(dst_path)
os.mkdir(dst_path)
file_num = 0
for file in files:
    if select_mode in file:
        img = cv2.imread(file)
        img = cv2.resize(img, (128, 256), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(os.path.join(dst_path, os.path.split(file)[1]), img)
        file_num += 1
print('file_num = %d' % file_num)