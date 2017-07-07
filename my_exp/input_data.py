import numpy as np
import math

class InputData:
	def __init__(self, imu_output, ground_truth):

		# class member values
		self.training_data = []
		self.training_ground_truth = []

		self.validation_data = []
		self.validation_ground_truth = []

		# ################## #
		# Parse the imu data #
		# ################## # 
		imu_file = open(imu_file, 'r')
		imu_data = []
		lines = imu_file.readlines()
		value = []
		for line in lines:
			if ('image' in line):
				if value:
					imu_data.append(value)
					value = []
			else:
				value.extend([float(i) for i in line.split()[1:]])
		self.imu_data = np.array(imu_data)

		# ###################### #
		# Parse the ground truth #
		# ###################### # 
		ground_truth = open(ground_truth,'r')
		ground_truth_pos = []
		lines = ground_truth.readlines()
		self.ground_truth_pos = np.array([float(i) for line in lines for i in line.split()[1:]]).reshape(:,7)



	def visualize_camera_pose(self):
		pass

	def 