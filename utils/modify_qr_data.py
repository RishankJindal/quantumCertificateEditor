import random
import re
from utils.constants import NEW_NAME

# Function to generate a random number with a given length
def generate_random_number(length):
    return ''.join(random.choices('0123456789', k=length))

# Function to modify the certificate number
def modify_certificate_number(cert_no):
    # Choose a random position to change
    position = random.randint(0, len(cert_no) - 1)
    # Choose how many digits to change (2 or 3)
    change_length = random.choice([2, 3])
    # Generate a new number with the same length as the original one
    new_digits = generate_random_number(len(cert_no))
    # Modify the certificate number at the chosen position
    modified_cert_no = cert_no[:position] + new_digits[position:position + change_length] + cert_no[position + change_length:]
    return modified_cert_no

def modify_qr_data(data):
    # Use regular expressions to extract the information
    pattern = re.compile(r"Certificate No\. - (\d+) Name - (.+?) Event - (.+)")
    # Match the pattern in the data string
    match = pattern.search(data)

    if match:
        certificate_no = match.group(1)
        name = match.group(2)
        event = match.group(3)

        # Create the dictionary
        info_dict = {
            "Certificate No.": certificate_no,
            "Name": name,
            "Event": event
        }

        # Modify certificate data
        info_dict['Certificate No.'] = modify_certificate_number(info_dict['Certificate No.'])
        info_dict['Name'] = NEW_NAME

        # Convert dictionary back to string
        data_string = ' '.join([f"{key} - {value}" for key, value in info_dict.items()])
        return data_string
    else:
        print("Pattern not found in the data")


