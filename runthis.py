import shutil
import os
from datetime import date
import pandas as pd
import sqlite3
import argparse
from util.helpers import message_parser

#--------------------------------- COPY SAMPLE FILES INTO /Archive/Original ---------------------------------#

# Define input and output directories
input_dir = './Archive/Original'
output_dir = './Archive/Modified'

# Create an argument parser for the command line
parser = argparse.ArgumentParser(description='Process input files.')

# Add arguments for input sample files
parser.add_argument('--input-csv', required=True, help='Path to sampledata.csv')
parser.add_argument('--input-adt', required=True, help='Path to ADT_sample.txt')
parser.add_argument('--input-oru', required=True, help='Path to Sample ORU.txt')

# Parse incoming arguments
args = parser.parse_args()

# If Archive directory and subdirectories don't exist, create them
if not os.path.exists(input_dir):
    os.makedirs(input_dir)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Destination for copies
destination_directory = os.path.join('Archive', 'Original')

# Files to copy
files_to_copy = [args.input_csv, args.input_adt, args.input_oru]

# Copy files
for file in files_to_copy:
    shutil.copy(file, destination_directory)

#--------------------------------- WRITE OUTPUT TO MODIFIED FILES IN /Archive/Modified ---------------------------------#

# Get today's date
current_date = date.today()

# Create the file names for the modified output files
adt_modified_filename = f"ADT_{current_date}_Modified_file.csv"
oru_modified_filename = f"ORU_{current_date}_Modified_file.csv"
orm_modified_filename = f"ORM_{current_date}_Modified_file.csv"

# Create dataframe for sample data
sample_data_df = pd.read_csv(f'{input_dir}/sampledata.csv')

# Create new columns for sample patients i.e. service date, full name
sample_data_df['date_of_service'] = current_date
sample_data_df['patient_name'] = sample_data_df['patient_last_name'] + ', ' + sample_data_df['patient_first_name'] + ' ' + sample_data_df['patient_middle_name']


# Create separate dataframes based on the message types i.e. ADT, ORU, ORM
adt_data_df = pd.DataFrame(sample_data_df[sample_data_df['message_type'].str[:3] == 'ADT'])
oru_data_df = pd.DataFrame(sample_data_df[sample_data_df['message_type'].str[:3] == 'ORU'])
orm_data_df = pd.DataFrame(sample_data_df[sample_data_df['message_type'].str[:3] == 'ORM'])

# Convert sample messages into lists
adt_message = open(f'{input_dir}/ADT_sample.txt', 'r').readlines()
oru_message = open(f'{input_dir}/Sample ORU.txt', 'r').readlines()

# Append data to appropriate dataframes using custom 'message_parser' function
adt_data_df = pd.concat([adt_data_df, pd.DataFrame(message_parser(adt_message))], ignore_index=True)
oru_data_df = pd.concat([oru_data_df, pd.DataFrame(message_parser(oru_message))], ignore_index=True)

# If we want to drop first, last, and middle name columns, use following lines. Else, comment out lines 74 and 75 ##
for df in [adt_data_df, oru_data_df, orm_data_df]:
    df.drop(columns = ['patient_first_name', 'patient_last_name', 'patient_middle_name'], inplace=True)

# Write the modified data to the output files
adt_data_df.to_csv(f'{output_dir}/{adt_modified_filename}', index=False)
oru_data_df.to_csv(f'{output_dir}/{oru_modified_filename}', index=False)
orm_data_df.to_csv(f'{output_dir}/{orm_modified_filename}', index=False)


#--------------------------------- CREATE A BILLING REPORT FILE.TXT ---------------------------------#

# Create a dataframe for total billing by state data
state_total_bill = sample_data_df.groupby('patient_state')['bill_amount'].sum().reset_index()

# Calculate the sum of the total bill amount and add it as a new row
total_sum = state_total_bill['bill_amount'].sum()
total_row = pd.DataFrame({'patient_state': ['TOTAL'], 'bill_amount': [total_sum]})
state_total_bill = pd.concat([state_total_bill, total_row], ignore_index=True)

# Write billing to output file
state_total_bill.to_csv(f'{output_dir}/state_total_bill.txt', index=False)

#--------------------------------- BONUS: IMPLEMENT SQLite ---------------------------------#

# Load adt data file
df = pd.read_csv(f'{output_dir}/{adt_modified_filename}')

# Clean Data
df.columns = df.columns.str.strip()

# Create/connect SQLite database
conn = sqlite3.connect('adt_patients.db')

# Load data to SQLite
df.to_sql('adt_patients', conn, if_exists='replace')

# Close connection
conn.close()
