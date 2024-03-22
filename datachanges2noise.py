import numpy as np
import matplotlib.pyplot as plt


# Load data from gamma.py and proton.py                                                                                                                       
gamma_data = np.load('gamma.npy')
proton_data = np.load('proton.npy')

# Plot histogram                                                                
plt.figure(figsize=(20, 10))
plt.hist([gamma_data, proton_data], bins=range(0, max(max(gamma_data), max(proton_data)) + 1), alpha=0.7, label=['Gamma', 'Proton'])
plt.xlim(500,2500)
plt.ylim(0,10)
plt.xlabel('Number of Change Points')
plt.ylabel('Number of Events')
plt.title('Histogram of Change Points')
plt.legend()
plt.savefig('Histogram of Change Points')#+str(i)+'.png')
