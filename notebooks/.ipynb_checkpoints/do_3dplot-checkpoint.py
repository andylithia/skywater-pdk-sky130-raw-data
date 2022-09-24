import scipy.io as sio
import numpy as np
from matplotlib import pyplot as plt
key = 'sky130_fd_pr__nfet_01v8_w7u_l0p18u_m1'
mat = sio.loadmat(key+'_ids_v_vg_vd.mat')

vd_list = mat['vd_list']
vg_list = mat['vg_list']
ids_list = mat['ids_list']

# Show (VGS, VDS) Coverage
my_cmap = plt.get_cmap('plasma')
fig = plt.figure(figsize = (10, 10))
ax = plt.axes(projection='3d')
ids_list_uA = list(e*1e6 for e in ids_list)
sctt3d = ax.scatter3D(vd_list, vg_list, ids_list_uA, c=ids_list, cmap = my_cmap, marker ='^')
ax.set_xlabel('VDS / V')
ax.set_ylabel('VGS / V')
ax.set_zlabel('IDS / uA')
ax.set_title(key)
ax.set_proj_type('ortho')
ax.view_init(45, -45)
plt.show()
plt.savefig(key+'_IDS_v_VGS_VDS.svg')
sctt3d_vg = ax.scatter3D(vd_list, vg_list, ids_list_uA, c=vd_list, cmap = my_cmap, marker ='^')
ax.view_init(0, 0)
plt.show()
plt.savefig(key+'_IDS_v_VGS.svg')

sctt3d_vd = ax.scatter3D(vd_list, vg_list, ids_list_uA, c=vg_list, cmap = my_cmap, marker ='^')
ax.view_init(0, -90)
plt.show()
plt.savefig(key+'_IDS_v_VDS.svg')