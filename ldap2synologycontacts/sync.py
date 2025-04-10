#!/usr/bin/env python3

import os
import requests

# CardDAV server details for Synology Contacts
CARD_DAV_URL = 'https://IP ADDRESS:5001/carddav/DOMAIN@@USERNAME/123123123123123123' #CHANGEME
USERNAME = 'USERNAME' #CHANGEME
PASSWORD = 'PASSWORD' #CHANGEME
VCF_DIRECTORY = 'vcards'

# Upload all new vCards from the specified directory
for file_name in os.listdir(VCF_DIRECTORY):
    if file_name.endswith('.vcf'):
        file_path = os.path.join(VCF_DIRECTORY, file_name)
        with open(file_path, 'r') as f:
            vcf_data = f.read()

        filename = os.path.basename(file_path)
        headers = {
            'Content-Type': 'text/vcard',
            'If-None-Match': '*',  # Avoids overwriting existing contacts
        }

        # Construct the URL for uploading the vCard
        url = f"{CARD_DAV_URL}/{filename}"

        response = requests.put(url, data=vcf_data, auth=(USERNAME, PASSWORD), headers=headers, verify=False)

        if response.status_code in [200, 201]:
            print(f"Successfully uploaded: {filename}")
        else:
            print(f"Failed to upload {filename}: {response.status_code} {response.text}")
