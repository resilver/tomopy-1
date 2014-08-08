# -*- coding: utf-8 -*-
"""
    This is a template script  for simple image processing tasks.
    For more functionality please check the documentation.
    
    Have fun!
    """
import tomopy
import os
import matplotlib.pyplot as mpl
import glob
import numpy as np

##_________________________inputs_and_parameters_______________________
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_043_ASU_small_beetle_A_dimax_2x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_43.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 5
num_proj = 800
chunk_size = 60
margin_slices = 20
num_chunk = np.int(num_proj/chunk_size) + 1
if num_proj == chunk_size:
    num_chunk = 1
    
z = 15
eng = 27.4
pxl = 5.5e-4  #for 2X lens
#pxl = 2.2e-4  #for 5X lens
rat = 5e-04  


center = 1034

##________________________rescale_for_16-bit_image____________________
data, white, dark, theta = tomopy.xtomo_reader(file_name, projections_start=1, slices_start=(num_proj/2), slices_end=(num_proj/2)+chunk_size)

d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta=theta)
d.zinger_removal(zinger_level=500, median_width=5)
d.normalize(negvals=1, cutoff=1)
d.stripe_removal()
d.center=center
d.gridrec()
d.apply_mask(ratio=0.95)

data_min = d.data_recon.min() 
data_max = d.data_recon.max()

##________________________reconstruction______________________________
for ii in xrange(num_chunk):
    if ii == 0:
        SliceStart = offset + ii*chunk_size
        SliceEnd = offset + (ii+1)*chunk_size
    else:
        SliceStart = offset + ii*(chunk_size-margin_slices)
        SliceEnd = offset + SliceStart + chunk_size
        if SliceEnd > (offset+num_proj):
            SliceEnd = offset+num_proj
            
    data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=SliceStart,slices_end=SliceEnd,white_start=3,white_end=9,dark_start=3,dark_end=9)
    data[0,:,:] = data[1,:,:]
    d.dataset(data, white, dark, theta)
    d.zinger_removal(median_width=15,zinger_level=200)
    d.normalize()
    d.correct_drift(10)
    d.stripe_removal(wname="sym16",level=10,sigma=4, padding=True)
    d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=False)
    d.center = center 
    d.gridrec()
    d.apply_mask(ratio=0.95)
    tomopy.xtomo_writer(d.data_recon[np.int(margin_slices/2):(SliceEnd-SliceStart-np.int(margin_slices/2)),:,:], output_file, dtype='uint16', axis=0, x_start=SliceStart+np.int(margin_slices/2), data_min=data_min, data_max=data_max, overwrite = True)
    d.FLAG_THETA = False










