import mean_shift as ms
#numpy module to reading file
import numpy as np	
#matplotlib module to plot data
import matplotlib.pyplot as plt 

KERNEL_BANDWIDTH = 1

#local sample data
original_points = np.genfromtxt('data.csv', delimiter=',')

#mean shift
mean_shifer = ms.MeanShift();
result = mean_shifer.cluster(original_points, KERNEL_BANDWIDTH);
shifted_data = result.shifted_points

#init figure
fig = plt.figure();

#original and shifted sub plot
original_sub_plot = fig.add_subplot(2, 1, 1);
original_sub_plot.set_title("original + shifted points ");
original_sub_plot.scatter(original_points[:,0], original_points[:,1], color='r');
original_sub_plot.scatter(shifted_data[:,0], shifted_data[:,1], color='g');

#shifted sub plot
shifted_sub_plot = fig.add_subplot(2, 1, 2);
shifted_sub_plot.set_title("shifted points");
shifted_sub_plot.scatter(shifted_data[:,0], shifted_data[:,1], color='g');

plt.show()
