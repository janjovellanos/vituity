import shutil
import os
from datetime import date
import pandas as pd
from utils.helpers import parseMessage

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

# Read the input csv files
sample_data_df = pd.read_csv(os.path.join(input_dir, 'sampledata.csv'))
# # adt_sample_df = pd.read_csv(os.path.join(input_dir, 'ADT_sample.txt'), sep='|')
# # oru_sample_df = pd.read_csv(os.path.join(input_dir, 'Sample ORU.txt'), sep='|')

# Set bill_amount for patients
# sample_data_df['date_of_service'] = current_date


# Create separate dataframes based on the message type prefixes i.e. ADT, ORU, ORM
adt_data_df = sample_data_df[sample_data_df['message_type'].str[:3] == 'ADT']
oru_data_df = sample_data_df[sample_data_df['message_type'].str[:3] == 'ORU']
orm_data_df = sample_data_df[sample_data_df['message_type'].str[:3] == 'ORM']

# Write the modified data to the output CSV files
# adt_data_df.to_csv(os.path.join(output_dir, adt_modified_filename), index=False)
# oru_data_df.to_csv(os.path.join(output_dir, oru_modified_filename), index=False)
# orm_data_df.to_csv(os.path.join(output_dir, orm_modified_filename), index=False)

# Step 2: Extract information from the txt files
adt_message = open('./Archive/Original/ADT_sample.txt', 'r').readlines()
oru_message = open('./Archive/Original/Sample ORU.txt', 'r').readlines()
# update_adt_df = adt_data_df.copy()
# update_oru_df = oru_data_df.copy()

# Loop through the lines of the TXT file and extract relevant information
# def parseMessage(message):
#     # bill_amount = 1234
#     # data = {'#': sample_data_df['#'].max() + 1}
#     data = {}
#     for segment in message:
#         if segment.startswith('MSH|'):
#             data['message_type'] = segment.split('|')[8].replace('^', '-')
#         elif segment.startswith('PID|'):
#             fields = segment.split('|')
#             data['patient_first_name'] = fields[5].split('^')[1]
#             data['patient_last_name'] = fields[5].split('^')[0]
#             data['patient_middle_name'] = fields[5].split('^')[2]
#             data['patient_address_1'] = fields[11].split('^')[0]
#             data['patient_state'] = fields[11].split('^')[3]
#             data['account_number'] = fields[3]
#     return [data]

adt_data_df = pd.concat([adt_data_df, pd.DataFrame(parseMessage(adt_message))], ignore_index=True)
oru_data_df = pd.concat([oru_data_df, pd.DataFrame(parseMessage(oru_message))], ignore_index=True)
adt_data_df.to_csv(f'./Archive/Modified/{adt_modified_filename}')
oru_data_df.to_csv(f'./Archive/Modified/{oru_modified_filename}')


# Step 4: Append the dictionary as a new row to the DataFrame
# for message in [adt_message, oru_message]:
#     # print(adt_message)
#     message_df = pd.DataFrame(parseMessage(message))
#     combined_df = pd.concat([combined_df, message_df], ignore_index=True)
#     combined_df.to_csv('./Archive/Original/sampledata.csv', index=False)

# updated_sample_data_df = pd.read_csv(os.path.join(input_dir, 'sampledata.csv'))

# Write the modified data to the output CSV files
# adt_data_df.to_csv(os.path.join(output_dir, adt_modified_filename), index=False)
# oru_data_df.to_csv(os.path.join(output_dir, oru_modified_filename), index=False)
# orm_data_df.to_csv(os.path.join(output_dir, orm_modified_filename), index=False)

# Set bill_amount for patients
# updated_sample_data_df['bill_amount'] = 1234


# Perform the required data manipulations
# For example, if you want to add a new column 'date_of_service' with today's date:
# sample_data_df['date_of_service'] = today_date

# Manipulate the 'patient_name' column as specified
# sample_data_df['patient_name'] = sample_data_df['patient_last_name'] + ', ' + sample_data_df['patient_first_name'] + ' ' + sample_data_df['patient_middle_name']

# Set bill_amount for patients
# sample_data_df['bill_amount'] = 1234

# sample_data_df = sample_data_df.drop(columns = ['patient_first_name', 'patient_last_name', 'patient_middle_name'])

# Create a report file in txt that lists the total bill amount for each state
# state_total_bill = sample_data_df.groupby('patient_state')['bill_amount'].sum().reset_index()
# state_total_bill.to_csv(os.path.join(output_dir, 'state_total_bill.txt'), sep='\t', index=False)

# Calculate the sum of the total bill amount and add it as a new row
# total_sum = state_total_bill['bill_amount'].sum()
# total_row = pd.DataFrame({'state': ['Total'], 'bill_amount': [total_sum]})
# state_total_bill = pd.concat([state_total_bill, total_row], ignore_index=True)

# Write the modified data to the output CSV files
adt_data_df.to_csv(os.path.join(output_dir, adt_modified_filename), index=False)
oru_data_df.to_csv(os.path.join(output_dir, oru_modified_filename), index=False)
orm_data_df.to_csv(os.path.join(output_dir, orm_modified_filename), index=False)
# state_total_bill.to_csv(os.path.join(output_dir, bill_report), index=False)
