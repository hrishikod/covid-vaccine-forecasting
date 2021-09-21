'''
This file contains helper functions for the program
'''
import pandas as pd
import datetime
import scipy.optimize

def generate_daily_differences(panda_data_frame_column, column_name):
	'''
	This function will take an input column and compute the differences 
	between each row and output another column
	'''
	inital_list = [panda_data_frame_column[0]]

	for index, row in enumerate(panda_data_frame_column.items()):
		if index > 0:
			inital_list.append(
				panda_data_frame_column[index]-panda_data_frame_column[index-1])

	column = pd.Series(inital_list)
	column.name = column_name
	return column


def calculate_date_difference(input_date):
	'''
	Calculates the difference in dates since the 14th of September
	'''
	date_format = "%d-%m-%Y"
	original_date = datetime.datetime.strptime("14-09-2021", date_format)
	new_date = datetime.datetime.strptime(input_date, date_format)

	date_diff = new_date-original_date

	return date_diff.days


def calculate_new_input_value(difference):
	'''
	Gets the new input value for the function
	WARNING!!!!!!!!! ORIGINAL END INDEX IS HARD CODED AS 207.... THIS IS BASED ON LENGTH OF DATASET
	'''
	# THIS IS DANGEROUS HERE, I KNOW... BUT I'M LAZY
	original_input_value = 207

	new_input_value = original_input_value + difference

	return new_input_value


def run_parameter_optimisation(logistic_function_vectorised, x_input, y_input, p0_array, bounds_array):
	'''
	Function for running the curve fit function function
	'''
	return optimize.curve_fit(logistic_function_vectorised, x_input, y_input, bounds=bounds_array, p0=p0_array)

