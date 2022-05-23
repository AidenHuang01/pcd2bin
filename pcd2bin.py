"""
Script to convert multiple PCD files into other formats using PCL
"""
import os
import subprocess

__author__ = "Sri Datta Budaraju"


# Make sure you have PCL installed
package = 'pcl_convert_pcd_ascii_binary'
input_dir = '/home/yucheng/workspace/WCSNG/pcd2bin/test04_17_wild6/mtlb-pcdFromBag/'
output_dir = '/home/yucheng/workspace/WCSNG/pcd2bin/output'

# Available conversion formats
asciiFormat = '0'
binaryFormat = '1'
binaryCompressedFormat = '2'
# Choosing binaryCompressedFormat
formatChoice = binaryCompressedFormat

for pcd in os.listdir(input_dir):
    # convert all PCD in input directory
    print('Converting pcd :', pcd)
    inputPCD = input_dir + '/' + pcd
    outputPCD = output_dir + '/' + pcd[:-4] + '.bin'

    # PCL command
    command = [package,
               inputPCD,
               outputPCD,
               formatChoice]

    subprocess.call(command)
    

os.remove(inputPCD)