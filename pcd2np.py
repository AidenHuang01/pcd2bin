import numpy as np 
import open3d as o3d
import os
from tqdm import tqdm

parent_path = './test04_17_wild6/mtlb-pcdFromBag/'
for file in tqdm(os.listdir(parent_path)):
    if file[-4:] != '.pcd':
        continue
    pcd_path = parent_path + file
    pcd = o3d.io.read_point_cloud(pcd_path)
    out_arr = np.asarray(pcd.points)  
    num_points = out_arr.shape[0]
    intensity = np.zeros((num_points, 1))
    out_arr = np.hstack((out_arr, intensity))
    out_arr[:,0] = -out_arr[:,0]
    output_file = file[:-4] + '.npy'
    np.save(output_file, out_arr) 
    # print('successfully converted ', output_file)