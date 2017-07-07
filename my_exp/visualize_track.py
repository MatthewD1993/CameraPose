import numpy as numpy
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import pandas as pd
import itertools
from mpl_toolkits.mplot3d import Axes3D

GROUND_TRUTH_FILE = '/home/cdeng/EuRoC/mav0/state_groundtruth_estimate0/data.csv'
groud_truth = pd.read_csv(GROUND_TRUTH_FILE)


fig = plt.figure()
fig.suptitle('Camera body tracking.')
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(groud_truth.ix[:,1].min(),groud_truth.ix[:,1].max())
ax.set_ylim(groud_truth.ix[:,2].min(),groud_truth.ix[:,2].max())
ax.set_zlim(groud_truth.ix[:,3].min(),groud_truth.ix[:,3].max())

start_point = groud_truth.ix[0,1:4].values
print (start_point)
plotpoints = groud_truth.ix[0,1:4].values
ax.scatter(*start_point, s=100, c='g', marker='v', label='origin')
scat = ax.scatter(*plotpoints,  c='r')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# ax.legend()

# colors = itertools.cycle(['r', 'y', 'b'])
def update(frame_number, groud_truth):
	global plotpoints, ax, scat
	plotpoints = [groud_truth.ix[:frame_number, 1].values, groud_truth.ix[:frame_number, 2].values, groud_truth.ix[:frame_number, 3].values]  
	# print (plotpoints)
	# print ('-------------------- ')
	scat = ax.scatter(*plotpoints,c='r')
	return plotpoints, scat





animation = FuncAnimation(fig, update, fargs=(groud_truth,), interval=1)

plt.show()