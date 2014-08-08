# -*- coding: utf-8 -*-
import tomopy





# file_name = '/local/data/Tapuia_dentary_ant3_M_200mm_4.hdf5'
# data, white, dark, theta = tomopy.xtomo_reader(file_name, projections_start=1, slices_start=300, slices_end=332)

# d = tomopy.xtomo_dataset(log='debug')
# d.dataset(data, white, dark, theta=theta)
# d.zinger_removal(zinger_level=500, median_width=5)
# d.normalize(negvals=1, cutoff=1)
# d.stripe_removal()
# d.phase_retrieval(alpha=0.005)
# d.center=1013.90625 
# d.gridrec(ringWidth=0)
# d.apply_mask(ratio=0.95)

# tomopy.xtomo_writer(d.data_recon, 'tmp/Tapuia_dentary_ant3_M_200mm_4/rec_', dtype='uint16', axis=0)






# file_name = '/local/data/Tapuia_max_bottom2_M_200mm_1.hdf5'
# data, white, dark, theta = tomopy.xtomo_reader(file_name, projections_start=1, slices_start=300, slices_end=332)

# d = tomopy.xtomo_dataset(log='debug')
# d.dataset(data, white, dark, theta=theta)
# d.zinger_removal(zinger_level=500, median_width=5)
# d.normalize(negvals=1, cutoff=1)
# d.stripe_removal()
# d.phase_retrieval(alpha=0.005)
# d.center=1043.4375
# d.gridrec(ringWidth=0)
# d.apply_mask(ratio=0.95)

# tomopy.xtomo_writer(d.data_recon, 'tmp/Tapuia_max_bottom2_M_200mm_1/rec_', dtype='uint16', axis=0)





# file_name = '/local/data/Tapuia_dentary_ant2_200mm_4.hdf5'
# data, white, dark, theta = tomopy.xtomo_reader(file_name, projections_start=1, slices_start=300, slices_end=332)

# d = tomopy.xtomo_dataset(log='debug')
# d.dataset(data, white, dark, theta=theta)
# d.zinger_removal(zinger_level=500, median_width=5)
# d.normalize(negvals=1, cutoff=1)
# # d.stripe_removal()
# d.phase_retrieval(alpha=0.005)
# d.center=1010
# d.gridrec(ringWidth=30)
# d.apply_mask(ratio=0.95)

# tomopy.xtomo_writer(d.data_recon, 'tmp/Tapuia_dentary_ant2_200mm_4_/rec_', dtype='uint16', axis=0)




file_name = '/local/data/Tapuiasaurus_dentary_ant_200mm_1.hdf5'
data, white, dark, theta = tomopy.xtomo_reader(file_name, projections_start=1, slices_start=300, slices_end=332)

d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta=theta)
d.zinger_removal(zinger_level=500, median_width=5)
d.normalize(negvals=1, cutoff=1)
d.stripe_removal()
d.phase_retrieval(alpha=0.005)
d.center=1010
d.gridrec(ringWidth=0)
d.apply_mask(ratio=0.95)

tomopy.xtomo_writer(d.data_recon, 'tmp/Tapuiasaurus_dentary_ant_200mm_1/rec_', dtype='uint16', axis=0)
