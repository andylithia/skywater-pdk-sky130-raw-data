import scipy.io as sio
import numpy as np
from matplotlib import pyplot as plt
key = 'sky130_fd_pr__nfet_01v8_w7u_l0p18u_m1'
mat = sio.loadmat(key+'_ids_v_vg_vd.mat')
vd_list_flatten = mat['vd_list_flatten']
vg_list_flatten = mat['vg_list_flatten']
ids_list_flatten = mat['ids_list_flatten']
sasb_list_flatten = mat['sasb_list_flatten']

# Show (VGS, VDS) Coverage
my_cmap = plt.get_cmap('plasma')
fig = plt.figure(figsize = (10, 10))
ax = plt.axes(projection='3d')
sctt3d = ax.scatter3D(vd_list_flatten, vg_list_flatten, list(e*1e6 for e in ids_list_flatten), c=sasb_list_flatten, cmap = my_cmap, marker ='^')

ax.set_xlabel('VDS / V')
ax.set_ylabel('VGS / V')
ax.set_zlabel('IDS / uA')
ax.set_title(key)
ax.set_proj_type('ortho')
plt.show()