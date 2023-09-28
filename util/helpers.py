import random

# Parses incoming list of lines from .txt file
def message_parser(message):
    # Preset bill amount and random '#' value
    data = {
        'bill_amount': 1234,
        '#': random.randint(201,999)
    }
    # Loop through list, parse and extract fields for new record to add into output files
    for segment in message:
        fields = segment.split('|')
        if segment.startswith('MSH|'):
            data['message_type'] = fields[8].replace('^', '-')
            data['message_time'] = f'{fields[6][8:10]}:{fields[6][10:12]}.0'
        elif segment.startswith('PID|'):
            data['id'] = fields[1]
            data['patient_first_name'] = fields[5].split('^')[1]
            data['patient_last_name'] = fields[5].split('^')[0]
            data['patient_middle_name'] = fields[5].split('^')[2]
            data['patient_address_1'] = fields[11].split('^')[0]
            data['patient_city'] = fields[11].split('^')[2]
            data['patient_state'] = fields[11].split('^')[3]
            data['patient_zip'] = fields[11].split('^')[4]
            data['patient_ssn'] = ''.join(fields[19].split('-'))
            data['account_number'] = fields[18]
            if len(fields[13].split('^')) > 8:
                data['patient_email_address'] = fields[13].split('^')[9]
    return [data]
