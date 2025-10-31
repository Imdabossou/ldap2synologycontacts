#!/usr/bin/env python3

import os
import requests

from config import carddav_url, carddav_username, carddav_password, carddav_vcf_directory

for file_name in os.listdir(carddav_vcf_directory):
    if file_name.endswith('.vcf'):
        file_path = os.path.join(carddav_vcf_directory, file_name)
        with open(file_path, 'r') as f:
            vcf_data = f.read()

        filename = os.path.basename(file_path)
        headers = {'Content-Type': 'text/vcard', 'If-None-Match': '*'}

        # Construct the URL for uploading the vCard
        url = f"{carddav_url}/{filename}"

        response = requests.put(url, data=vcf_data, auth=(carddav_username, carddav_password), headers=headers, verify='synology.pem')

        # Print logs
        if response.status_code == 201:
            print(f"Successfully uploaded: {filename}")
        if response.status_code == 412:
            print(f"Contact already exists {filename}")
    else:
        print(f"Failed to upload {filename}: {response.status_code} {response.text}")

test
