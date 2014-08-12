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

######################### you input section - Start #########################
# file location
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_020_Zophobas_morio_adult_05_0A_dimax_5x_150mm_76ms_1.0DegPerSec_360Deg_100umLuAG_27.4keV_BHutch' 
file = 'proj_20.hdf'

# set trial range for searching correct num_overlap _pixels
nop_start = 630
nop_end = 645

# how many field of view corrected sclies should be reconstructed once
fov_per_pass = 10

# set the range of slices to be reconstructed; chunk_size is for preventing memory usage overflow that can slow down reconstructions significantly
offset = 0
num_slices = 600
chunk_size = 60
margin_slices = 20
#offset = 500
#num_slices = 10
#chunk_size = 10
#margin_slices = 0
num_chunk = np.int(num_slices/chunk_size) + 1
if num_slices == chunk_size:
    num_chunk = 1

# phase retrieval parameters
z = 15.
eng = 27.
pxl = 5.5e-4  #for 2X lens
#pxl = 2.2e-4  #for 5X lens
rat = 5e-04 
######################### you input section - End #########################

######################### initialization - Start #########################
file_name = os.path.join(data_dir, file)
output_file = data_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'
log_filename = data_dir+'/recon_'+file.split(".")[-2]+'/'+file.split(".")[-2] +'.log'

# object d is for containing data that will be used for phase retrieval 
d = tomopy.xtomo_dataset(log='debug')
# object d_recon is for containing data for reconstruction
d_recon = tomopy.xtomo_dataset(log='debug')
######################### initialization - End #########################

########################## finding num_overlap_pixels - Start #########################
#### phase retrieval - Start ####
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=300,slices_end=310,white_start=3,white_end=9,dark_start=3,dark_end=9)
data[0,:,:] = data[1,:,:]       # in case the first projection image is corrupted

d.dataset(data, white, dark, theta)
d.normalize()
d.stripe_removal(wname="db5",level=10,sigma=4.)
data_size = d.data.shape
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True) 
data_tem = d.data
#### phase retrieval - End ####

#### trial recons - Start ####
for ii in range(nop_start,nop_end):
    d.dataset(data_tem,np.ones([d.data.shape[1],d.data.shape[2]]),None,None)
    d.correct_fov(num_overlap_pixels=ii)
#    tomopy.xtomo_writer(d.data[:,5:7,:], output_file+'sinogram_num_overlap_pixel_'+str(ii)+'_', axis=1,x_start=0,overwrite = True)
#    d.FLAG_THETA = False

    d_recon.dataset(d.data,np.ones([d.data.shape[1],d.data.shape[2]]),None,None)
#    print ii,d.data.shape,d_recon.data.shape
    d_recon.center = d_recon.data.shape[2]/2.0
    d_recon.gridrec()
#    print d_recon.center
    tomopy.xtomo_writer(d_recon.data_recon[5:7,:,:], output_file+'num_overlap_pixel_'+str(ii)+'_', axis=0,x_start=0,overwrite = True)
    d.FLAG_THETA = False
#### trial recons - Start ####
######################### finding num_overlap_pixels - End #########################

