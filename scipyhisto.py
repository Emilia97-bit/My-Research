import numpy as np
import matplotlib.pyplot as plt


# Load data from gamma.py and proton.py

gamma_data = np.load('gamma.npy')
proton_data = np.load('proton.npy')

#print(np.load('gamma.npy'))
#print(np.load('proton.npy'))

# Plot histogram                                                                                                                                              
plt.figure(figsize=(20, 10))
plt.hist([gamma_data, proton_data], bins=range(0, max(max(gamma_data), max(proton_data)) + 1), alpha=0.7, label=['Gamma', 'Proton'])
#plt.hist([gamma_data, proton_data], bins=20, alpha=0.7, label=['Gamma', 'Proton'])

#plt.hist(gamma_data, bins=20, alpha=0.7, label='Gamma')
#plt.hist(proton_data, bins=20, alpha=0.7, label='Proton')
plt.xlim(5400,6800)
plt.ylim(0,16)
plt.xlabel('Number of peaks per event')
plt.ylabel('Number of event')
plt.title('Histogram of Change Points')
plt.legend()
plt.savefig('Histogram of peaks finding2')
