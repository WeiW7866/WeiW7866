# Suomi National Polar-orbiting Partnership(S-NPP)

import datetime as dt                                               # Python standard library datetime  module
import numpy as np
from netCDF4 import Dataset                                         # http://code.google.com/p/netcdf4-python/
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid
import os.path

inputfn_dir = '/data01/jyin/4test/NPPCloud/NCfl'
outputfn_dir = '/data01/jyin/4test/NPPCloud/Binaryfmt'

#count = 0

for year in range(2018, 2019):
    year_str = f"{year:04}"
    print(year_str)
    for month in range(10, 11):
        month_str = f"{month:02}"
        for day in range(1, 32):
            count = 0
            day_str = f"{day:02}"
            date_str = year_str + month_str + day_str
            fn = 'ncfilename' + date_str + '.txt'
            print(date_str)
            full_input_path = inputfn_dir + '/' + year_str + '/' + date_str
            ftxt = full_input_path + '/' + fn
            with open(ftxt, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    count += 1
                    ncfl = full_input_path + '/' + line.strip()
                    nt_str = f"{count:04}"
                    foutn = 'Cloudbinary' + date_str + '_' + nt_str + '.dat'
                    full_output_path = outputfn_dir + '/' + foutn
                    if os.path.exists(ncfl):
                        nc_fid = Dataset(ncfl, 'r')
                        lats = nc_fid.variables['Latitude'][:]
                        lons = nc_fid.variables['Longitude'][:]
                        sst = nc_fid.variables['CloudProbability'][:][:]
                        dat = np.array([lats, lons, sst])
                        print(sst.shape)
                        f=open(full_output_path,"wb")
                        f.write(dat)
                        f.close()
