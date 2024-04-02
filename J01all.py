import datetime as dt
import numpy as np
import h5py
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid
import os.path
import glob


inputfn_dir = 'xxxxxxxx'
outputfn_dir = 'xxxxxxxxx'

for year in range(20xx, 20xx):
    year_str = f"{year:04}"
    print(year_str)
    for month in range(10, 11):
        month_str = f"{month:02}"
        for day in range(1, 32):
            count = 0
            day_str = f"{day:02}"
            date_str = year_str + month_str + day_str
            fn = 'hdffln' + date_str + '.txt'
            full_input_path = inputfn_dir + '/' + year_str + '/' + date_str
            ftxt = full_input_path + '/' + fn
            with open(ftxt, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    count += 1
                    nt_str = f"{count:02}"
                    hdf = full_input_path + '/' + line.strip()
                    foutn = 'J1MVTb' + date_str + '_' + nt_str + '.dat'
                    output_fn = full_input_path + '/' + foutn
                    if os.path.exists(hdf):
                        with h5py.File(hdf, 'r') as f:
                            a_group_key = list(f.keys())[0]
                            G1 = f.get('All_Data')
                            G2 = G1.get('VIIRS-MOD-GEO_All')
                            lat = np.array(G2.get('Latitude'))
                            lon = np.array(G2.get('Longitude'))
                            G2SVM12= G1.get('VIIRS-M12-SDR_All')
                            TbSVM12= np.array(G2SVM12.get('BrightnessTemperature'))
                            G2SVM13= G1.get('VIIRS-M13-SDR_All')
                            TbSVM13= np.array(G2SVM13.get('BrightnessTemperature'))
                            G2SVM14= G1.get('VIIRS-M14-SDR_All')
                            TbSVM14= np.array(G2SVM14.get('BrightnessTemperature'))
                            G2SVM15= G1.get('VIIRS-M15-SDR_All')
                            TbSVM15= np.array(G2SVM15.get('BrightnessTemperature'))
                            G2SVM16= G1.get('VIIRS-M16-SDR_All')
                            TbSVM16= np.array(G2SVM16.get('BrightnessTemperature'))
                            f.close()
                            dat = np.array([lat, lon, TbSVM12, TbSVM13, TbSVM14, TbSVM15, TbSVM16])
                            print(dat.shape)
                            f=open(output_fn,"wb")
                            f.write(dat)
                            f.close()
        #file.close()

