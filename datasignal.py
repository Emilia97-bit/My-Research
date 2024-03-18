import matplotlib as mpl
mpl.use('Svg')  
import numpy as np
import matplotlib.pyplot as plt
import ruptures as rpt

from ctapipe.io import EventSource
from ctapipe.utils import get_dataset_path
from ctapipe.visualization import CameraDisplay

particle = 'Gamma'
if particle=="Gamma":
    source = EventSource("/lfs/l7/hess/users/steinmassl/MC_phase2d3_production/Diffuse_benedetta_new/ref0.79/"+particle+"/20deg/0deg/0.0deg/Data/gamma_20deg_0deg_run21410___phase2d_simon3_desert-all_tel-_mix_atm_new_trig_thresh-sims-realnsb_benedettanew0903_cone5.simhess.gz",focal_length_choice='EQUIVALENT')

        
elif particle=="Proton":
    source = EventSource("/lfs/l7/hess/users/steinmassl/MC_phase2d3_production/Diffuse_benedetta_new/ref0.79/"+particle+"/20deg/0deg/0.0deg/Data/proton_20deg_0deg_run21610___phase2d_simon3_desert-all_tel-_mix_atm_new_trig_thresh-sims-realnsb_benedettanew0903.simhess.gz",focal_length_choice='EQUIVALENT')


#print(source)
event_iterator = iter(source)

for i in np.arange(5):
    event = next(event_iterator)
    #print(event.r0.tel.keys())

    teldata = event.r0.tel[5]




    # generate signal                                      
    n_samples, dim, sigma = 1000, 3, 4
    n_bkps = 4#number of breakpoints, points where signal changes its beh
    #signal, bkps = rpt.pw_constant(n_samples, dim, n_bkps, noise_std=sigma)

    # detection                                                                                                                                    
    #algo = rpt.Pelt(model="rbf").fit(teldata.waveform[0,0:])
   # result = algo.predict(pen=10)

    if teldata.waveform is not None:
        algo = rpt.Pelt(model="l2").fit(teldata.waveform[0,0,:])
        result = algo.predict(pen=8)
        print(result)
        
        #print(result) #This line prints the detected change points.                 
    # display                                                                                            
        rpt.display(teldata.waveform[0,0,:], result)
        plt.savefig('Waveforml2pen8'+str(i)+'.png')
