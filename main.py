# Same functionality as processPlot.py however splitting into functions so they can be called from a GUI

# Import statements
import heartpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import heartpy as py
from scipy.signal import find_peaks

# User information variables
age = 23
length = 0.75
gender = 'male'

# Read data from CSV and store in data frame
data = pd.read_csv('dataStoreNew.csv')


def pwvCalculation(data, length):

    # Retrieve data
    D = data.to_numpy();
    t = D[:,0]
    ECG = D[:,1]
    PPG = D[:,2]

    # Removes first 5 data entries from arrays as contain incorrect data as sensor is setting up
    t = t[5:]
    ECG = ECG[5:]
    PPG = PPG[5:]

    # Filtering Data to remove noise
    ECG = heartpy.remove_baseline_wander(ECG,200)

    # Normalising PPG data
    normalizedPPG = (PPG-PPG.min())/ (PPG.max() - PPG.min())

    # Normalising ECG data
    normalizedECG = (ECG-ECG.min())/ (ECG.max() - ECG.min())

    # Finding peaks in PPG data
    peaksPPG, _ = find_peaks(normalizedPPG, distance=100, prominence=0.05)

    # Finding peaks in ECG data
    peaksECG, _ = find_peaks(normalizedECG, distance=100, prominence=0.2)

    print(peaksPPG)
    print(peaksECG)

    PWV = [None] * len(peaksPPG)
    sampleDiff = [None] * len(peaksPPG)
    timeDiff = [None] * len(peaksPPG)
    # Calculating time difference between peaks and hence PWV
    for i in range(0, len(peaksPPG)):
        sampleDiff[i] = peaksPPG[i] - peaksECG[i]
        timeDiff[i] = sampleDiff[i] / 200
        PWV[i] = length / timeDiff[i];

    print(sampleDiff)
    print(timeDiff)
    print(PWV)
    # Returns average PWV value
    print('Average PWV of user is: ', (sum(PWV) / len(PWV)))
    return sum(PWV) / len(PWV)



def pwvComparison(age, gender, pwv):

    if gender == 'male':
        if 10 <= age <= 19:
            if 3.46 <= pwv <= 4.04:
                return 'Healthy'
            else:
                return 'Outside of healthy range'
        elif 20 <= age <= 29:
            if 3.51 <= pwv <= 4.09:
                return 'Healthy'
            else:
                return 'Outside of healthy range'
        elif 30 <= age <= 39:
            if 3.56 <= pwv <= 4.14:
                return 'Healthy'
            else:
                return 'Outside of healthy range'
        elif 40 <= age <= 49:
            if 3.61 <= pwv <= 4.19:
                return 'Healthy'
            else:
                return 'Outside of healthy range'
        elif 50 <= age <= 59:
            if 3.66 <= pwv <= 4.24:
                return 'Healthy'
            else:
                return 'Outside of healthy range'
        elif 60 <= age <= 69:
            if 3.71 <= pwv <= 4.29:
                return 'Healthy'
            else:
                return 'Outside of healthy range'

    if gender == 'female':
        if 10 <= age <= 19:
            if 3.24 <= pwv <= 3.74:
                return 'Healthy'
            else:
                return 'Outside of healthy range'
        elif 20 <= age <= 29:
            if 3.30 <= pwv <= 3.80:
                return 'Healthy'
            else:
                return 'Outside of healthy range'
        elif 30 <= age <= 39:
            if 3.36 <= pwv <= 3.86:
                return 'Healthy'
            else:
                return 'Outside of healthy range'
        elif 40 <= age <= 49:
            if 3.42 <= pwv <= 3.92:
                return 'Healthy'
            else:
                return 'Outside of healthy range'
        elif 50 <= age <= 59:
            if 3.48 <= pwv <= 3.98:
                return 'Healthy'
            else:
                return 'Outside of healthy range'
        elif 60 <= age <= 69:
            if 3.55 <= pwv <= 4.05:
                return 'Healthy'
            else:
                return 'Outside of healthy range'



# Calling functions
pwvCalculation(data, length)





# Plotting
#fig = plt.figure()
#ax = fig.subplots(3)
# PPG Signal
#ax[0].plot(normalizedPPG, label='Normalized PPG')
# ECG Signal
#ax[1].plot(normalizedECG, label='Normalized ECG')

# Combined plot with peaks shown
#ax[2].plot(normalizedPPG, label='Normalized PPG')
#ax[2].scatter(peaksPPG, normalizedPPG[peaksPPG], color = 'r', s = 10, marker = 'x', label = 'PPG maxima')
#ax[2].plot(normalizedECG, label='Normalized ECG')
#ax[2].scatter(peaksECG, normalizedECG[peaksECG], color = 'b', s = 10, marker = 'x', label = 'ECG maxima')
#ax[2].legend()
#ax[2].grid()
#plt.show()


