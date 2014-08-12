# -*- coding: utf-8 -*-

# This script is meant to allow a user to call a function in terminal to reconstruct a sample. 

import tomopy
import os
import matplotlib.pyplot as mpl
import glob
import numpy as np

# This function 
def recon_180(data_dir='.', file = 'out.h5', output_dir='/Volumes/Socha_MP8/', num_proj=1800, startSlice=None, endSlice=None, z=15, eng=27.4, lens=2, center=None):
    
    ##_________________________inputs_and_parameters_______________________

    file_name = os.path.join(data_dir, file)
    output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

    d = tomopy.xtomo_dataset(log='debug')
    
    # Program does not complete a sample if actual number of slices is input. This somewhat arbitrary scaled value seems to work well.
    #num_proj = (3/2)*num_proj
    # These values work well with the computer's available memory and produce quality images.
    chunk_size = 60
    margin_slices = 20

    # Define pixel size from function argument lens. 
    pxl = 0
    if lens == 2:
        pxl = 5.5e-4  #for 2X lens
    elif lens == 5:
        pxl = 2.2e-4  #for 5X lens
    
    rat = 5e-04  
    
    num_chunk = np.int(num_proj/chunk_size) + 1
    if num_proj == chunk_size:
        num_chunk = 1
    
    #Set defalt start and end slice values.
    if endSlice == None:
        endSlice = num_proj
    if startSlice == None:
        startSlice=0
        offset = startSlice 
    else:
        offset = startSlice - (margin_slices/2)

    ##________________________rescale_for_16-bit_image____________________
    data, white, dark, theta = tomopy.xtomo_reader(file_name, projections_start=1, slices_start=(num_proj/2), slices_end=(num_proj/2)+chunk_size)

    d = tomopy.xtomo_dataset(log='debug')
    d.dataset(data, white, dark, theta=theta)
    #d.zinger_removal(zinger_level=500, median_width=5)
    d.normalize(negvals=1, cutoff=1)
    # Helps minimize ring artifacts.
    d.stripe_removal()
    
    # Finds center of rotation
    if center == None:
        d.optimize_center(ratio=1)
    else:
        d.center=center
    
    d.gridrec()

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
            if SliceEnd >= (endSlice-(margin_slices/2)) and SliceEnd < (endSlice-margin_slices+chunk_size):
                SliceEnd = (endSlice-(margin_slices/2))
            if SliceEnd >= (endSlice-margin_slices+chunk_size):
                break                
            
        data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=SliceStart,slices_end=SliceEnd,white_start=3,white_end=9,dark_start=3,dark_end=9)
        data[0,:,:] = data[1,:,:]
        d.dataset(data, white, dark, theta)
        #d.zinger_removal(median_width=10)
        d.normalize()
        d.correct_drift(10)
        d.stripe_removal(wname="sym16",level=11,sigma=2)
        d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
        
        # Finds center of rotation
        if center == None:
            d.optimize_center(ratio=0.8)
        else:
            d.center=center
        
        d.gridrec()
        d.apply_mask(ratio=0.95)
       
        #data[0,:,:] = data[1,:,:]
        #d = tomopy.xtomo_dataset(log='debug')
        #d.dataset(data, white, dark, theta)
        ##d.zinger_removal(median_width=15,zinger_level=200)
        #d.normalize()
        ##d.stripe_removal(wname="sym16",level=10,sigma=2)
        ##d.stripe_removal(level=10,sigma=1)
        #d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
        ##d.stripe_removal(wname="sym16",level=10,sigma=4)
        #data_size = d.data.shape
        ##d.median_filter(10)
        ##d.optimize_center(ratio=0.3) 
        ##print d.center

        tomopy.xtomo_writer(d.data_recon[np.int(margin_slices/2):(SliceEnd-SliceStart-np.int(margin_slices/2)),:,:], output_file, dtype='unit16', axis=0, x_start=SliceStart+np.int(margin_slices/2), data_min=data_min, data_max=data_max, overwrite=True)
        d.FLAG_THETA = False
    print 'Finished reconstructing slices from ' + file
    

    
#############################################################################################################

# Specify the directory in which your data file is located.
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_015_Schistocerca_gregaria_19_leg3_dimax_5x_150mm_76ms_1.0DegPerSec_360Deg_100umLuAG_27.4keV_BHutch'

# Specify the data file name.
file = 'proj_15.hdf'

# Specify the directory in which you would like the reconstructed slices to be saved.
output_dir = data_dir

# Number of y pixels in input data file.
num_proj = 1200

# The number slice to start the reconstruction at.
startSlice = 170

# The number slice to end the reconstruction at.
endSlice = 200

# Distance between sample and scintilator in centimeters.
z = 15

# Energy of x-ray beam in KeV.
eng = 27.4

# Magnification of lens used.(Input 2 or 5 for a 2x lens or 5x lens, respectively.)
lens = 5

# Center 
center = 1028

#_______________________________RECONSTRUCTION_______________________________________________

# Call the reconstruction function.
recon_180(data_dir=data_dir, file=file, output_dir=output_dir, num_proj=num_proj, startSlice=startSlice, endSlice=endSlice, z=z, eng=eng, lens=lens, center=center)






