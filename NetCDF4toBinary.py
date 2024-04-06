# Convert NetCDF4 to Binary format
# Developed by Wei Wang on 04/02/2022
# wangwei20160708@gmail.com

import datetime as dt                                               # Python standard library datetime  module
import numpy as np
from netCDF4 import Dataset                                         # http://code.google.com/p/netcdf4-python/
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid
import os.path

inputfn_dir = 'This is a input directory'
outputfn_dir = 'This is a output directory'

#count = 0

for year in range(2012, 2020):
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
                        lats = nc_fid.variables['Latitude'][:]                                                          # Attribute Latitude
                        lons = nc_fid.variables['Longitude'][:]                                                         # Attribute Longitude
                        cpb = nc_fid.variables['CloudProbability'][:][:]                                                # Attribute Cloud Probability, please replace it for your purpose
                        dat = np.array([lats, lons, cpb])
                        print(cpb.shape)
                        
                        f=open(full_output_path,"wb")
                        f.write(dat)
                        f.close()
