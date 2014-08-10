# -*- coding: utf-8 -*-

# This script is meant to allow a user to call a function in terminal to reconstruct a sample. 

import tomopy
import os
import matplotlib.pyplot as mpl
import glob
import numpy as np

# This function 
def recon_180(data_dir='.', file = 'out.h5', output_dir='.', num_proj=1800, startSlice=startSlice, endSlice=endSlice, z=15, eng=27.4, lens=2, center=None, center=center):
    
    ##_________________________inputs_and_parameters_______________________

    file_name = os.path.join(data_dir, file)
    output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

    d = tomopy.xtomo_dataset(log='debug')
    
    # Program does not complete a sample if actual number of slices is input. This somewhat arbitrary scaled value seems to work well.
    num_proj = (3/2)*num_proj
    # These values work well with the computer's available memory and produce quality images.
    chunk_size = 60
    margin_slices = 20
    
    num_chunk = np.int(num_proj/chunk_size) + 1
    if num_proj == chunk_size:
        num_chunk = 1
    
    if pxl == 2:
        pxl = 5.5e-4  #for 2X lens
    elif pxl == 5:
        pxl = 2.2e-4  #for 5X lens
    
    rat = 5e-04  
    
    #Set defalt start and end slice values.
    if endSlice == None:
        endSlice = num_proj
    if startSlice == None:
        startSlice=0
    offset = startSlice

    ##________________________rescale_for_16-bit_image____________________
    data, white, dark, theta = tomopy.xtomo_reader(file_name, projections_start=1, slices_start=(num_proj/3), slices_end=(num_proj/3)+chunk_size)

    d = tomopy.xtomo_dataset(log='debug')
    d.dataset(data, white, dark, theta=theta)
    d.zinger_removal(zinger_level=500, median_width=5)
    d.normalize(negvals=1, cutoff=1)
    # Helps minimize ring artifacts.
    d.stripe_removal()
    
    # Finds center of rotation
    if center == None:
        d.optimize_center(ratio=1)
    else:
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
        if SliceEnd > endSlice:
            SliceEnd = endSlice
            
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

