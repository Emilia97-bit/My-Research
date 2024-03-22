import matplotlib.pylab as pylab
import numpy as np
import matplotlib
matplotlib.use('Svg')
from matplotlib import pyplot as plt
import ruptures as rpt
from scipy import signal
plt.style.use('tableau-colorblind10')

params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
          'axes.titlesize':'xx-large',
          'xtick.labelsize':'xx-large',
          'ytick.labelsize':'xx-large'}

from ctapipe.io import EventSource
from ctapipe.utils import get_dataset_path
from ctapipe.visualization import CameraDisplay

particle = 'Gamma'

if particle=="Gamma":
    source = EventSource("/lfs/l7/hess/users/steinmassl/MC_phase2d3_production/Diffuse_benedetta_new/ref0.79/"+particle+"/20deg/0deg/0.0deg/Data/gamma_20deg_0deg_run21410___phase2d_simon3_desert-all_tel-_mix_atm_new_trig_thresh-sims-realnsb_benedettanew0903_cone5.simhess.gz",focal_length_choice='EQUIVALENT')

elif particle=="Proton":
    source = EventSource("/lfs/l7/hess/users/steinmassl/MC_phase2d3_production/Diffuse_benedetta_new/ref0.79/"+particle+"/20deg/0deg/0.0deg/Data/proton_20deg_0deg_run21610___phase2d_simon3_desert-all_tel-_mix_atm_new_trig_thresh-sims-realnsb_benedettanew0903.simhess.gz",focal_length_choice='EQUIVALENT')

event_iterator = iter(source)
num_changes_per_event = []
count=0
for event in event_iterator:
    total_changes = 0
    print(count)
    if count>1000:
        break
    count+=1
    teldata = event.r0.tel[5]

    if teldata.waveform is not None:
        for pixel_id in range(1764):
            if np.amax(teldata.waveform[0,pixel_id,:]) > 300:
        
            
                waveform = teldata.waveform[0,pixel_id,:]
            
                # Applying change finder algorithm
                algo = rpt.Pelt(model="l2").fit(waveform)
                result = algo.predict(pen=2)
    
                total_changes += len(result)
    print(total_changes)
    num_changes_per_event.append(total_changes)  # Appending the total changes  


np.save('gamma.npy',np.asarray(num_changes_per_event))
