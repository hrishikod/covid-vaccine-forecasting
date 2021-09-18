from vaccination_forecaster_io import *

data_file_path = "data"
file_name = "covid_vaccine.xlsx"


def vaccination_model():
	clean_table = return_clean_table(data_file_path, file_name)
	print(clean_table)

if __name__=='__main__':
	vaccination_model()


