import pandas as pd
import os



def build_path(file_location, file_name):
	'''
	This function builds the filepath
	'''
	path = os.path.join(file_location, file_name)

	return path

def read_excel_table(path):
	'''
	This function reads the excel sheet for the data
	'''
	input_table = pd.read_excel(path, engine="openpyxl")
	return input_table


def clean_excel_table(table):
	'''
	This function cleans the excel table input
	'''
	cleaned_table = table.dropna(axis=0)

	return cleaned_table


def return_clean_table(file_location, file_name):
	path = build_path(file_location, file_name)
	initial_table = read_excel_table(path)
	cleaned_table = clean_excel_table(initial_table)

	return cleaned_table

