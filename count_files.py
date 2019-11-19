import numpy as np
import os
print('Here are the folder counts:')
count_empty_files = 0
for item in os.listdir('VGGFaces2Cropped/train'):
    #print(item)
    item_count = int(os.system('ls VGGFaces2Cropped/train/%s'%item+' | wc -l'))
    #print(item_count)
