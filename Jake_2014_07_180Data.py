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

data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_015_Schistocerca_gregaria_19_leg3_dimax_5x_150mm_76ms_1.0DegPerSec_360Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_15.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 730
num_proj = 1200
chunk_size = 60
margin_slices = 20
num_chunk = np.int(num_proj/chunk_size) + 1
if num_proj == chunk_size:
    num_chunk = 1
    
z = 15
eng = 27.4
#pxl = 5.5e-4  #for 2X lens
pxl = 2.2e-4  #for 5X lens
rat = 5e-04   

###----------------- finding center/media/Socha_2014_07/2014_07
#data, white, dark, theta = #tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
#data[0,:,:] = data[1,:,:]
#d = tomopy.xtomo_dataset(log='debug')
#d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=10)
#d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
#d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
##d.stripe_removal(wname="sym16",level=10,sigma=4)
#data_size = d.data.shape
##d.median_filter(10)
##d.optimize_center(ratio=0.3) 
##print d.center         
#d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+70,center_step=0.5)


center = 1028


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
    d.zinger_removal(median_width=10)
    d.normalize()
    d.correct_drift(10)
    d.stripe_removal(wname="sym16",level=10,sigma=4)
    d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
    d.center = center 
    d.gridrec()
    
    tomopy.xtomo_writer(d.data_recon[np.int(margin_slices/2):(SliceEnd-SliceStart-np.int(margin_slices/2)),:,:], output_file, axis=0,dtype='float32', x_start=SliceStart+np.int(margin_slices/2),overwrite = True)
    d.FLAG_THETA = False










