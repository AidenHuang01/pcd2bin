import numpy as np 
import open3d as o3d

pcd = o3d.io.read_point_cloud("./0038.pcd")
out_arr = np.asarray(pcd.points)  
num_points = out_arr.shape[0]
intensity = np.zeros((num_points, 1))
out_arr = np.hstack((out_arr, intensity))
print("output array from input list : ", out_arr)  
print("out_arr.shape: ", out_arr.shape)
np.save('0038.npy', out_arr) 

python demo.py --cfg_file cfgs/kitti_models/pv_rcnn.yaml \
    --ckpt pointpillar_7728.pth \
    --data_path ../0038.npy