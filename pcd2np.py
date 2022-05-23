import numpy as np 
import open3d as o3d

pcd = o3d.io.read_point_cloud("./0038.pcd")
out_arr = np.asarray(pcd.points)  
num_points = out_arr.shape[0]
intensity = np.zeros((num_points, 1))
out_arr = np.hstack((out_arr, intensity))
out_arr[:,0] = -out_arr[:,0]
print("output array from input list : ", out_arr)  
print("out_arr.shape: ", out_arr.shape)
np.save('0038_flip_x.npy', out_arr) 