import random

# Parses incoming list of lines from .txt file
def message_parser(message):
    # data = {'#': sample_data_df['#'].max() + 1}
    # Preset bill amount
    data = {
        'bill_amount': 1234,
        '#': random.randint(100,999)
    }
    # Loop through list and extract required fields
    for segment in message:
        if segment.startswith('MSH|'):
            data['message_type'] = segment.split('|')[8].replace('^', '-')
        elif segment.startswith('PID|'):
            fields = segment.split('|')
            data['patient_first_name'] = fields[5].split('^')[1]
            data['patient_last_name'] = fields[5].split('^')[0]
            data['patient_middle_name'] = fields[5].split('^')[2]
            data['patient_address_1'] = fields[11].split('^')[0]
            data['patient_state'] = fields[11].split('^')[3]
            data['account_number'] = fields[3]
    return [data]
