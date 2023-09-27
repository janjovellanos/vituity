import shutil
import os
from datetime import date
import pandas as pd
from utils.helpers import message_parser

#--------------------------------- COPY ALL FILES INTO /Archive/Original ---------------------------------#

# Source path of files being used
source_directory = os.path.expanduser('~/Desktop')

# Define the source file paths
csv_file = os.path.join(source_directory, 'sampledata.csv')
adt_file = os.path.join(source_directory, 'ADT_sample.txt')
oru_file = os.path.join(source_directory, 'Sample ORU.txt')

# Destination for copies
destination_directory = os.path.join(source_directory, 'vituity_take_home', 'Archive', 'Original')

# Files to copy
files_to_copy = [csv_file, adt_file, oru_file]

# Copy files
for file in files_to_copy:
    shutil.copy(file, destination_directory)

#--------------------------------- CREATE NEW MODIFIED FILES IN /Archive/Modified ---------------------------------#

# Define input and output directories
input_dir = './Archive/Original'
output_dir = './Archive/Modified'

# Get today's date
current_date = date.today()

# Create the file names for the modified output files
adt_modified_filename = f"ADT_{current_date}_Modified_file.csv"
oru_modified_filename = f"ORU_{current_date}_Modified_file.csv"
orm_modified_filename = f"ORM_{current_date}_Modified_file.csv"

# Create dataframe for sample data
sample_data_df = pd.read_csv(os.path.join(input_dir, 'sampledata.csv'))

# Create separate dataframes based on the message types i.e. ADT, ORU, ORM
adt_data_df = sample_data_df[sample_data_df['message_type'].str[:3] == 'ADT']
oru_data_df = sample_data_df[sample_data_df['message_type'].str[:3] == 'ORU']
orm_data_df = sample_data_df[sample_data_df['message_type'].str[:3] == 'ORM']

# Extract data from the txt files
adt_message = open('./Archive/Original/ADT_sample.txt', 'r').readlines()
oru_message = open('./Archive/Original/Sample ORU.txt', 'r').readlines()

# Append data to appropriate dataframes using custom 'message_parser' function
adt_data_df = pd.concat([adt_data_df, pd.DataFrame(message_parser(adt_message))], ignore_index=True)
oru_data_df = pd.concat([oru_data_df, pd.DataFrame(message_parser(oru_message))], ignore_index=True)

# adt_data_df.map(lambda x: int(x) if pd.notna(x) and isinstance(x, int) else x)
# oru_data_df.map(lambda x: int(x) if pd.notna(x) and isinstance(x, int) else x)

# Add new columns as requested i.e. service date, full name
adt_data_df['date_of_service'] = current_date
oru_data_df['date_of_service'] = current_date
adt_data_df['patient_name'] = adt_data_df['patient_last_name'] + ', ' + adt_data_df['patient_first_name'] + ' ' + adt_data_df['patient_middle_name']
oru_data_df['patient_name'] = oru_data_df['patient_last_name'] + ', ' + oru_data_df['patient_first_name'] + ' ' + oru_data_df['patient_middle_name']

# Write the modified data to the output files
adt_data_df.to_csv(f'{output_dir}/{adt_modified_filename}', index=False)
oru_data_df.to_csv(f'{output_dir}/{oru_modified_filename}', index=False)
orm_data_df.to_csv(f'{output_dir}/{orm_modified_filename}', index=False)

# If we want to drop first, last, middle name columns, use following example -->
# *_data_df = *_data_df.drop(columns = ['patient_first_name', 'patient_last_name', 'patient_middle_name'])

#--------------------------------- CREATE A REPORT FILE.TXT, THAT LISTS TOTAL BILL AMOUNT BY STATE ---------------------------------#

# Create a report file that lists the total bill amount for each state
state_total_bill = sample_data_df.groupby('patient_state')['bill_amount'].sum().reset_index()
state_total_bill.to_csv(f'{output_dir}/state_total_bill.txt', sep='\t', index=False)

# Calculate the sum of the total bill amount and add it as a new row
total_sum = state_total_bill['bill_amount'].sum()
total_row = pd.DataFrame({'patient_state': ['TOTAL'], 'bill_amount': [total_sum]})
state_total_bill = pd.concat([state_total_bill, total_row], ignore_index=True)

state_total_bill.to_csv(f'{output_dir}/state_total_bill.txt', index=False)
