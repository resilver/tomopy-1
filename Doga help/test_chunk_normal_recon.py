# -*- coding: utf-8 -*-
import tomopy



file_name = '/local/data/Tapuia_dentary_ant3_M_200mm_4.hdf5'


slices_start = 300
chunk_size = 32 # keep it reasoably large depending on the available memory
for m in range(4): # change range manually 4*32 slices will be reconstructed starting from 300
	data, white, dark, theta = tomopy.xtomo_reader(file_name, projections_start=1, slices_start=slices_start, slices_end=slices_start+chunk_size)

	d = tomopy.xtomo_dataset(log='debug')
	d.dataset(data, white, dark, theta=theta)
	d.zinger_removal(zinger_level=500, median_width=5)
	d.normalize(negvals=1, cutoff=1)
	d.stripe_removal()
	d.center=1013.90625 
	d.gridrec()
	d.apply_mask(ratio=0.95)

    # use the first chunks min max value for all chunks
	if m == 0:
	    data_min = d.data_recon.min() 
	    data_max = d.data_recon.max()

	tomopy.xtomo_writer(d.data_recon, 'tmp/test/rec_', dtype='uint16', axis=0, x_start=slices_start, data_min=data_min, data_max=data_max)
	slices_start += chunk_size