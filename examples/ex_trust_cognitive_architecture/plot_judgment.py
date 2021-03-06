#!/usr/bin/python

## Massimiliano Patacchiola, Plymouth University 2017
# https://mpatacchiola.github.io
# This script plot a bar-chart for the mean and std obtained
# in the judgment test with children and robots. It prints the mean and std. 
#
# Judgment: two informants (reliable and unreliable) give different labels
# to 3 new objects. The child has to say which informant was not good
# at answering questions. Correct if child indicates unreliable informant.

import numpy as np
import matplotlib.pyplot as plt

#Experimental distribtuions obtained through simulated agents
#Learning rate 0.1, informant reputation counter not updated when child_confidence==0
sample_4yo_array = np.array([1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]) #20 samples
sample_3yo_array = np.array([1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]) #20 samples

#4yo Mean,  3yo Mean
my_mean = (np.mean(sample_4yo_array), np.mean(sample_3yo_array))
my_mean_std = (np.std(sample_4yo_array), np.std(sample_3yo_array))

#Data of the original experiment of Harris et al.
#4yo Mean Original, 3yo Mean Original
original_mean = (0.83, 0.74)
original_mean_std = (0.30, 0.37)

print("----- 4-years-old -----")
print("Mean: " + str(np.mean(sample_4yo_array)))
print("Std: " + str(np.std(sample_4yo_array)))
print("")
print("----- 3-years-old -----")
print("Mean: " + str(np.mean(sample_3yo_array)))
print("Std: " + str(np.std(sample_3yo_array)))
print("")


index = np.array([1, 2])
bar_width = 0.35

error_config = dict(ecolor='black', lw=0.5, capsize=5, capthick=1, ls = 'dotted') #= {'ecolor': '0.3'}

rects1 = plt.bar(index, my_mean, bar_width,
                 alpha=1.0,
                 color='white',
                 error_kw=error_config,
                 yerr=my_mean_std,
                 hatch="/",
                 label='Robot')

rects2 = plt.bar(index + bar_width, original_mean, bar_width,
                 alpha=1.0,
                 color='white',
                 error_kw=error_config,
                 yerr=original_mean_std,
                 hatch="x",
                 label='Children')


#Set the labels
font_size = 15
#plt.title('Scores by group and gender')
plt.ylabel('Correct Answers (Mean)', size=font_size)
#plt.xlabel('Children Group (Age)', size=font_size)
plt.gca().yaxis.grid(True)
plt.xticks(index + bar_width, ('4-years-old', '3-years-old'), size=font_size)

#Hide the X ticks
ax = plt.axes()
ax.xaxis.set_ticks_position('none') 
#ax.xaxis.set_ticks(range(0, 11, 1))
#Set axis limit
border = 0.8 #defines the border space
ax.set_xlim([index[0]+bar_width-border, index[1]+bar_width+border])
ax.set_ylim([0, 2])

#Setup the legend
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),ncol=3, fancybox=True, shadow=True)

plt.tight_layout()

plt.savefig("fig_robot_children_comparison_judgment.jpg", dpi=500)


