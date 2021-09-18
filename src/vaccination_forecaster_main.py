from vaccination_forecaster_io import *
import datetime
import math
import numpy as np
import scipy.optimize as optimize
import matplotlib.pyplot as plt

data_file_path = "data"
file_name = "covid_vaccine.xlsx"

def generate_daily_differences(panda_data_frame_column,column_name):
	'''
	This function will take an input column and compute the differences 
	between each row and output another column
	'''
	inital_list = [panda_data_frame_column[0]]	

	for index, row in enumerate(panda_data_frame_column.items()):
		if index > 0:
			inital_list.append(panda_data_frame_column[index]-panda_data_frame_column[index-1])


	column = pd.Series(inital_list)
	column.name = column_name
	return column


########### NEEDS WORK ############################
def date_generator(start_date_string,end_date_string):
	start_date = datetime.datetime.strptime(start_date_string, "%d-%m-%Y")
	end_date = datetime.datetime.strptime(end_date_string, "%d-%m-%Y")
	dates_generated = [start_date+datetime.timedelta(days=x) for x in range(0,(end_date-start_date).days+1)]

	return dates_generated

def vaccination_model():
	'''
	Main model file
	'''
	clean_table = return_clean_table(data_file_path, file_name)
	
	daily_first_vaccines = generate_daily_differences(clean_table.people_vaccinated, "daily_first_vaccines")
	daily_second_vaccines = generate_daily_differences(
		clean_table.people_fully_vaccinated, "daily_second_vaccines")
	

	############ COULD BE MADE INTO A FUNCTION ##############
	start_date = datetime.date(2021, 9, 14)
	number_of_days = 17

	date_list = [(start_date + datetime.timedelta(days=day)).isoformat() for day in range(number_of_days)]

	print(date_list)

	###########################################################


if __name__=='__main__':
	vaccination_model()


