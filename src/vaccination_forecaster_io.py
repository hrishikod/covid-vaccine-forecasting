import pandas as pd
import os

data_file_path = "../data"
file_name = "covid_vaccine.xlsx"


def read_excel_table(file_name,file_location):
	'''
	This function reads the excel sheet for the data
	'''
	input_table = pd.read_excel("data/covid_vaccine.xlsx", engine="openpyxl")
	return input_table


def clean_excel_table(table):
	'''
	This function cleans the excel table input
	'''
	cleaned_table = table.dropna(axis=0)

	return cleaned_table

clean_table = clean_excel_table(input_table)

print(clean_table)
