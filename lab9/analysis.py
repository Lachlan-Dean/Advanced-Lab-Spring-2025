import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from nptdms import TdmsFile

# Reading in the file where janzen stomped and jogged down the hall
data_file = 'Stomp_then_jog.tdms'
thisTDMS = TdmsFile.read(data_file)

### These next lines are from the github link provided ###

# Extract the Measurement group.
group = thisTDMS['Measurement']
# Extract the acquisition properties.
props = thisTDMS.properties

# Assign relevant acquisition properties to variables.
samplingFrequency   = int( props['SamplingFrequency[Hz]'] )
spatialSampling     = props['SpatialResolution[m]']
gaugeLength         = props['GaugeLength']
measureLength       = props['MeasureLength[m]']
startTime           = props['GPSTimeStamp'].astype('M8[ms]').astype('O')

# Load the raw data into a numpy array object.
acousticData = np.asarray( [group[channel].data for channel in group] )

# Print out the dimensions of the array.
numberChannels  = acousticData.shape[0]
numberSamples   = acousticData.shape[1]

# Unscale raw counts to engineering units, nanostrain rate.
nanoStrainRate  = 116 * 2**-13 * samplingFrequency / gaugeLength * acousticData

### End of lines copied from github ###
t_index = 50
t_index_2 = 51
t_index_3 = 52

strain_profile1 = nanoStrainRate[:, t_index]
strain_profile2 = nanoStrainRate[:, t_index_2]
strain_profile3 = nanoStrainRate[:, t_index_3]

distance = np.linspace(0, 512, 512)

fig, ax = plt.subplots(1,1, figsize=(10,10))
ax.plot(distance, strain_profile3)
ax.set_xlim(100,400)
ax.set_ylim(-10000,10000)

ax.set_ylabel('Nanostrain Rate')
ax.set_xlabel('Distance Along Fiber (m)')
plt.show()
