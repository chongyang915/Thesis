################################################################################
# Description: Script to analyze the learning algorithm convergence
# Author:      Pierpaolo Necchi
# Email:       pierpaolo.necchi@gmail.com
# Date:        dom 19 giu 2016 18:01:13 CEST
################################################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('seaborn-colorblind')

##############
# Parameters #
##############

inputDir = '../../Data/Debug/Single_Synth_RN_P0_F0_S0_N5/ARAC/'
nExperiments = 10

########################
# Visualize allocation #
########################

df = pd.read_csv(inputDir + 'experiment0.csv')

# Read backtest data

# Temporary variables
rSum   = np.zeros(len(df))
r2Sum  = np.zeros(len(df))
sSum   = np.zeros(len(df))
s2Sum  = np.zeros(len(df))
shSum  = np.zeros(len(df))
sh2Sum = np.zeros(len(df))

for i in xrange(nExperiments):

    df = pd.read_csv(inputDir + 'experiment' + str(i) + '.csv')

    rSum += df['average'].values
    r2Sum += df['average'].values * df['average'].values
    sSum += df['stdev'].values
    s2Sum += df['stdev'].values * df['stdev'].values
    shSum += df['sharpe'].values
    sh2Sum += df['sharpe'].values * df['sharpe'].values

rMean = rSum / float(nExperiments)
rDev  = np.sqrt(r2Sum / float(nExperiments) - rMean * rMean)
sMean = sSum / float(nExperiments)
sDev  = np.sqrt(s2Sum / float(nExperiments) - sMean * sMean)
shMean = shSum / float(nExperiments)
shDev  = np.sqrt(sh2Sum / float(nExperiments) - shMean * shMean)

fig = plt.figure(figsize=(15,5), facecolor='white', edgecolor='black')

ax1 = fig.add_subplot(131)
ax1.plot(df['epoch'].values, rMean, lw=2, c='black')
ax1.plot(df['epoch'].values, rMean + rDev, lw=2, ls=':', c='black')
ax1.plot(df['epoch'].values, rMean - rDev, lw=2, ls=':', c='black')
ax1.set_ylabel('Average Reward')
ax1.set_xlabel('Training Epoch')

ax2 = fig.add_subplot(132)
ax2.set_title('Learning Algorithm', fontsize=18)
ax2.plot(df['epoch'].values, sMean, lw=2, c='black')
ax2.plot(df['epoch'].values, sMean + sDev, lw=2, ls=':', c='black')
ax2.plot(df['epoch'].values, sMean - sDev, lw=2, ls=':', c='black')
ax2.set_ylabel('Reward Standard Deviation')
ax2.set_xlabel('Training Epoch')

ax3 = fig.add_subplot(133)
ax3.plot(df['epoch'].values, shMean, lw=2, c='black')
ax3.plot(df['epoch'].values, shMean + shDev, lw=2, ls=':', c='black')
ax3.plot(df['epoch'].values, shMean - shDev, lw=2, ls=':', c='black')
ax3.set_ylabel('Sharpe Ratio')
ax3.set_xlabel('Training Epoch')

plt.tight_layout()
plt.show()
