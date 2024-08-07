
import os
print('wow')

group_ICA_path = '/export/home/ranigera/IDCH-rsfMRI/data/group_ICA'
rs_data_path = '/export/home/ranigera/IDCH-rsfMRI/data/pre_proc_data'
# list all files in all subdirectories of rs_data_path
rs_data_files = []
for root, dirs, files in os.walk(rs_data_path):
    for file in files:
        if file.endswith('.nii.gz'):
            rs_data_files.append(os.path.join(root, file))
print('Number of files:', len(rs_data_files))
# create input_files.txt
input_files = os.path.join(group_ICA_path, 'input_files.txt')


with open(input_files, 'w') as f:
    for file in rs_data_files:
        f.write(file + '\n')
