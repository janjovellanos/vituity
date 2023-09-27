import pandas as pd
from datetime import date
import os
import shutil
import shutil
import os
from datetime import date
import pandas as pd   # Define the source file paths


# Creating Modified Files ##########################################################

# Define the input and output directories
input_dir = "./Original"
output_dir = "./Modified"
print("Output Directory:", os.path.abspath(output_dir))


today_date = date.today().strftime("%Y%m%d")

# Create the file names for the ADT and ORU modified files
adt_modified_filename = f"ADT_{today_date}_Modified_file.csv"
oru_modified_filename = f"ORU_{today_date}_Modified_file.csv"
orm_modified_filename = f"ORM_{today_date}_Modified_file.csv"
bill_report = f"Bill_Report.txt"

# Read the input ADT and ORU CSV files using Pandas
sample_data_df = pd.read_csv(
    r'C:\Users\potos\Desktop\jans_project\Archive\Original\sampledata.csv')


# Extract the first 3 characters of 'message_type' into a new column 'message_type_prefix'
sample_data_df['message_type_prefix'] = sample_data_df['message_type'].str[:3]

# Perform the required data manipulations
# For example, if you want to add a new column 'date_of_service' with today's date:
sample_data_df['date_of_service'] = today_date

# Manipulate the 'patient_name' column as specified
sample_data_df['patient_name'] = sample_data_df['patient_last_name'] + ', ' + \
    sample_data_df['patient_first_name'] + ' ' + \
    sample_data_df['patient_middle_name']

# Set bill_amount for patients
sample_data_df['bill_amount'] = 1234

sample_data_df = sample_data_df.drop(
    columns=['patient_first_name', 'patient_last_name', 'patient_middle_name'])

# Create separate DataFrames based on the message type prefixes
adt_sample_data_df = sample_data_df[sample_data_df['message_type_prefix'] == 'ADT']
oru_sample_data_df = sample_data_df[sample_data_df['message_type_prefix'] == 'ORU']
orm_sample_data_df = sample_data_df[sample_data_df['message_type_prefix'] == 'ORM']


# Create a report file in txt that lists the total bill amount for each state
state_total_bill = sample_data_df.groupby(
    'patient_state')['bill_amount'].sum().reset_index()
state_total_bill.to_csv(os.path.join(
    output_dir, 'state_total_bill.txt'), sep='\t', index=False)

# Calculate the sum of the total bill amount and add it as a new row
total_sum = state_total_bill['bill_amount'].sum()
total_row = pd.DataFrame({'state': ['Total'], 'bill_amount': [total_sum]})
state_total_bill = pd.concat([state_total_bill, total_row], ignore_index=True)

# adt_sample_data_df = adt_sample_data_df['message_type', 'patients_name']

# Write the modified data to the output CSV files
adt_sample_data_df.to_csv(os.path.join(
    output_dir, adt_modified_filename), index=False)
oru_sample_data_df.to_csv(os.path.join(
    output_dir, oru_modified_filename), index=False)
orm_sample_data_df.to_csv(os.path.join(
    output_dir, orm_modified_filename), index=False)
state_total_bill.to_csv(os.path.join(output_dir, bill_report), index=False)
Collapse
New_Text_Document_9.txt
4 KB
﻿
Hector
xhect
