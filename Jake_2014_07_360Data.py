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
data_dir = '/Volumes/Socha_MP8/2014_07/2-BM/2014_07_010_Zophobas_morio_adult_05_head_dimax_5x_150mm_76ms_1.0DegPerSec_360Deg_100umLuAG_27.4keV_BHutch' 
file = 'proj_10.hdf'

# set trial range for searching correct num_overlap _pixels
nop_start = 624
nop_end = 640

# how many field of view corrected sclies should be reconstructed once
fov_per_pass = 10

# set the range of slices to be reconstructed; chunk_size is for preventing memory usage overflow that can slow down reconstructions significantly
offset = 0
num_slices = 768
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

#nop = 612.0


######################### reconstructing volume - Start #########################
#for ii in xrange(num_chunk):
#    if ii == 0:
#        SliceStart = offset + ii*chunk_size
#        SliceEnd = offset + (ii+1)*chunk_size
#    else:
#        SliceStart = offset + ii*(chunk_size-margin_slices)
#        SliceEnd = SliceStart + chunk_size
#        if SliceEnd > (offset + num_slices):
#            SliceEnd = offset + num_slices
#    
#    print SliceStart, SliceEnd       
#    data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=SliceStart,slices_end=SliceEnd,white_start=3,white_end=9,dark_start=3,dark_end=9)
#    data[0,:,:] = data[1,:,:]
#    d.dataset(data, white, dark, theta)
#    d.zinger_removal(median_width=15,zinger_level=500)
#    d.normalize()
#    d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#    d.stripe_removal(wname="db5",level=7,sigma=4.)
#    data_tem = d.data
#    
#    sub_chunk = int(np.fix((SliceEnd - SliceStart - 0.01)/10.0) + 1)
#    
#    for jj in range(sub_chunk):
#        sub_chunk_start = jj*fov_per_pass
#        sub_chunk_end = (jj+1)*fov_per_pass
#        if sub_chunk_end > data_tem.shape[1]:
#            sub_chunk_end = data_tem.shape[1]
#            
#        if (sub_chunk_end >np.int(margin_slices/2)):  
#            d.dataset(data_tem[:,sub_chunk_start:sub_chunk_end,:],np.ones([(sub_chunk_end - sub_chunk_start),d.data.shape[2]]),None,None)
#            d.correct_fov(num_overlap_pixels=nop)
#            d_recon.dataset(d.data,np.ones([d.data.shape[1],d.data.shape[2]]),None,None)
#            d_recon.center = d_recon.data.shape[2]/2.0
#            d_recon.gridrec()
##            d_recon.remove_background()
#            d_recon.remove_gaussian_background(sigma=30.0)
#            
#            d_recon_write_start = 0 
#            d_recon_write_x_start = SliceStart + sub_chunk_start
#            if (sub_chunk_end - np.int(margin_slices/2)) < fov_per_pass:
#                d_recon_write_start = sub_chunk_end - np.int(margin_slices/2)
#                d_recon_write_x_start = SliceStart + np.int(margin_slices/2)
#            tomopy.xtomo_writer(d_recon.data_recon[d_recon_write_start:,:,:], 
#                                output_file, axis=0,
#                                x_start=d_recon_write_x_start,
#                                overwrite = True)
#            d.FLAG_THETA = False

    
    
######################## reconstructing volume - End #########################


######################### logging reconstruction settings - Start #########################
#### You may need to modify the below log contents manually. You can also add or delete the items as your desires
#log_file = open(log_filename,'wa')
#log_file.write('------ ' + file.split(".")[-2] + ' reconstruction parameters ------\n')
#log_file.write('\n')
#log_file.write('flat-field correction: ' + 'True\n')
#log_file.write('dark-field correction: ' + 'True\n')
#log_file.write('phase retrieval: ' + 'True\n')
#log_file.write('phase retrieval algrithm: ' + 'Paganin\n')
#log_file.write('    det-sam distance: ' + str(z) + 'cm\n')
#log_file.write('    x-ray engergy: ' + str(eng) + 'keV\n')
#log_file.write('    detector pixel size: ' + str(pxl) + 'cm\n')
#log_file.write('    beta/delta: ' + str(rat) + '\n')
#log_file.write('stripe removal: ' + 'False\n')
#log_file.write('    wavelet name: ' + 'db5\n')
#log_file.write('    filtering level: ' + '12\n')
#log_file.write('    sigma: ' + '4\n')
#log_file.write('zinger removal: ' + 'True\n')
#log_file.write('    median filter width: ' + str(15) + 'pixels\n')
#log_file.write('    zinger level: ' + str(500) + '\n')
#log_file.write('normalize: ' + 'True\n')
#log_file.write('correct_shift: ' + 'False\n')
#log_file.write('auto-centering: ' + 'False\n')
#log_file.write('gridrec: ' + 'True\n')
#log_file.write('reconstruction region: \n')
#log_file.write('    slice start: ' + str(offset) + '\n')
#log_file.write('    slice end: ' + str(offset+num_slices-1) + '\n')
#log_file.write('recon center: ' + str(center) + '\n')
#log_file.close()

######################### logging reconstruction settings - End #########################


