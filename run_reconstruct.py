## This is meant to be coppied and pasted into terminal to run. This shows how to call the recon_180 function to reconstruct slices of a 180 degrees data sample. This script will produce 16-bit .tif images. 

%run reconstruct.py

#________________________________INPUTS_AND_PARAMETERS_________________________________________

# Specify the directory in which your data file is located.
data_dir = '/Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_015_Schistocerca_gregaria_19_leg3_dimax_5x_150mm_76ms_1.0DegPerSec_360Deg_100umLuAG_27.4keV_BHutch'

# Specify the data file name.
file = 'proj_15.hdf'

# Specify the directory in which you would like the reconstructed slices to be saved.
output_dir =' /Volumes/Socha_MP8/2014_07_working_tomo_data_2-BM/2-BM/2014_07_015_Schistocerca_gregaria_19_leg3_dimax_5x_150mm_76ms_1.0DegPerSec_360Deg_100umLuAG_27.4keV_BHutch/recon_test'
# Number of y pixels in input data file.
num_proj = 1200

# The number slice to start the reconstruction at.
startSlice = 700

# The number slice to end the reconstruction at.
endSlice = 750

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


