# This file is for stitching json results from multiple folders to one result json file
import os
import json
import numpy

file_path = '/mnt/Data/CLASP-Activity-Dataset/20190930/cam22exp2_res/'
res_list = os.listdir(file_path+'results/')
res_list.sort()

data_all = []
for res in res_list:
    with open(file_path+'results/'+res) as f:
        data_all = data_all + json.load(f)

# Test data_all
# for data in data_all:
#     print(data['image_id'])
with open(file_path+'alphapose-results.json','w') as outfile:
    json.dump(data_all, outfile)

print("Well Done!")
