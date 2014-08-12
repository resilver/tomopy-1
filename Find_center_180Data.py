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
"""

#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_026_Zophobas_morio_adult_05_F_dimax_5x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_26.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+95,center_step=0.5)

#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_027_Zophobas_morio_adult_05_G_dimax_5x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_27.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+95,center_step=0.5)

#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_028_Zophobas_morio_adult_05_H_dimax_5x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_28.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+95,center_step=0.5)

#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_029_Zophobas_morio_adult_05_I_dimax_5x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_29.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+95,center_step=0.5)


#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_030_Zophobas_morio_adult_05_J_dimax_5x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_30.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+95,center_step=0.5)


#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_031_Zophobas_morio_pupa_01_A_dimax_5x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_31.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+95,center_step=0.5)


#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_032_Zophobas_morio_pupa_01_B_dimax_2x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_32.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+95,center_step=0.5)

#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_033_Zophobas_morio_pupa_01_C_dimax_2x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_Bhutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_33.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+95,center_step=0.5)

#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_035_Zophobas_morio_pupa_01_E_dimax_2x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_35.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+95,center_step=0.5)

#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_036_Zophobas_morio_pupa_01_F_dimax_2x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_36.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+95,center_step=0.5)

#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_037_Zophobas_morio_pupa_01_G_dimax_2x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_37.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+95,center_step=0.5)

#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_038_Zophobas_morio_pupa_01_H_dimax_2x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_38.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+95,center_step=0.5)

#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_039_Zophobas_morio_pupa_01_I_dimax_2x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_39.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+95,center_step=0.5)


#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_040_Zophobas_morio_pupa_01_J_dimax_2x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_40.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+51,center_end=data_size[2]/2+60,center_step=0.5)


#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_041_Zophobas_morio_pupa_01_K_dimax_2x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_41.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+51,center_end=data_size[2]/2+60,center_step=0.5)


#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_042_Zophobas_morio_pupa_01_L_dimax_2x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_42.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+51,center_end=data_size[2]/2+60,center_step=0.5)


#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_043_ASU_small_beetle_A_dimax_2x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_43.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+70,center_step=0.5)


#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_044_ASU_small_beetle_B_dimax_2x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_44.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+70,center_step=0.5)


#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_045_ASU_small_beetle_C_dimax_2x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_45.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+70,center_step=0.5)


#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_046_ASU_small_beetle_D_dimax_2x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_46.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+70,center_step=0.5)


#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_047_ASU_small_beetle_E_dimax_2x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_Bhutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_47.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+70,center_step=0.5)


#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_048_ASU_small_beetle_F_dimax_2x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_48.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+70,center_step=0.5)


#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_049_ASU_small_beetle_G_dimax_2x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_Bhutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_49.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 50
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+70,center_step=0.5)

"""
#############################################################################################################
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_049_ASU_small_beetle_G_dimax_2x_150mm_76ms_1.0DegPerSec_180Deg_100umLuAG_27.4keV_BHutch'

output_dir =  data_dir
# the directory to look into
file = 'proj_49.hdf'
file_name = os.path.join(data_dir, file)
output_file = output_dir+'/recon_'+file.split(".")[-2]+'/recon_'+file.split(".")[-2] +'_'

d = tomopy.xtomo_dataset(log='debug')

offset = 10
num_proj = 600
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

####----------------- finding center/media/Socha_2014_07/2014_07
data, white, dark, theta = tomopy.xtomo_reader(file_name,slices_start=200,slices_end=220,white_start=3,white_end=9,dark_start=1,dark_end=4)
data[0,:,:] = data[1,:,:]
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
#d.zinger_removal(median_width=15,zinger_level=200)
d.normalize()
#d.stripe_removal(wname="sym16",level=10,sigma=2)
#d.stripe_removal(level=10,sigma=1)
d.phase_retrieval(dist=z, energy=eng, pixel_size=pxl, alpha=rat,padding=True)
#d.stripe_removal(wname="sym16",level=10,sigma=4)
data_size = d.data.shape
#d.median_filter(10)
#d.optimize_center(ratio=0.3) 
#print d.center         
d.diagnose_center(dir_path=data_dir+'/data_center/',center_start=data_size[2]/2+50,center_end=data_size[2]/2+70,center_step=0.5)


