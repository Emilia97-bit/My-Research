import matplotlib.pylab as pylab
import numpy as np
import matplotlib
matplotlib.use('Svg')
from matplotlib import pyplot as plt
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

particle = 'Proton'

if particle=="Gamma":
    source = EventSource("/lfs/l7/hess/users/steinmassl/MC_phase2d3_production/Diffuse_benedetta_new/ref0.79/"+particle+"/20deg/0deg/0.0deg/Data/gamma_20deg_0deg_run21410___phase2d_simon3_desert-all_tel-_mix_atm_new_trig_thresh-sims-realnsb_benedettanew0903_cone5.simhess.gz",focal_length_choice='EQUIVALENT')

elif particle=="Proton":
    source = EventSource("/lfs/l7/hess/users/steinmassl/MC_phase2d3_production/Diffuse_benedetta_new/ref0.79/"+particle+"/20deg/0deg/0.0deg/Data/proton_20deg_0deg_run21610___phase2d_simon3_desert-all_tel-_mix_atm_new_trig_thresh-sims-realnsb_benedettanew0903.simhess.gz",focal_length_choice='EQUIVALENT')

print(source) 
event_iterator = iter(source)

for i in np.arange(10):
    event = next(event_iterator)
    #print(event.r0.tel.keys())


    ######################################################################
    # now, we have a larger event with many telescopes… Let’s look at one of
    # them:
    teldata = event.r0.tel[5]
    fig=plt.figure(figsize=(10,10))

    if teldata.waveform is not None:
        #print(np.shape(teldata.waveform))
        for j in range(1764):
            #print(teldata.waveform[0,j,:])
            plt.plot(teldata.waveform[0,j,:],alpha=0.5)

                        
    #x=np.radom.randint(100) #Plots random numbers
    #plt.scatter(x,x)
    plt.xlabel("Sample")
    plt.ylabel("Amplitude [p.e.]")
    
    plt.tight_layout()
    plt.savefig(particle+'/'+str(i)+'.png')
