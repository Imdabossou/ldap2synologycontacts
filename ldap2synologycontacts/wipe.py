#!/usr/bin/env python3

import requests
import xml.etree.ElementTree as ET
import urllib.parse

CARD_DAV_URL = 'https://IP ADDRESS:5001/carddav/DOMAIN@@USERNAME/123123123123123123' #CHANGEME
USERNAME = 'USERNAME' #CHANGEME
PASSWORD = 'PASSWORD' #CHANGEME

response = requests.request(
    'PROPFIND', CARD_DAV_URL,
    auth=(USERNAME, PASSWORD),
    headers={'Depth': 'infinity'},
    verify=False
)

print("Response Status Code:", response.status_code)

if response.status_code == 207:
    tree = ET.ElementTree(ET.fromstring(response.text))
    root = tree.getroot()

    namespaces = {
        'd': 'DAV:',
        'CR': 'urn:ietf:params:xml:ns:carddav'
    }

    contact_urls = []
    for href in root.findall('.//d:href', namespaces):
        href_text = href.text
        # Only delete .vcf files, skipping the Administrator.vcf and collection root.
        if (
            href_text.endswith('.vcf') and
            'Administrator.vcf' not in href_text
        ):
            contact_urls.append(href_text)

    if not contact_urls:
        print("No deletable contacts found.")

    for contact_url in contact_urls:
        # Use urljoin without additional quote to avoid double encoding.
        full_contact_url = urllib.parse.urljoin(CARD_DAV_URL, contact_url)
        print(f"Attempting to delete: {full_contact_url}")

        del_response = requests.delete(full_contact_url, auth=(USERNAME, PASSWORD), verify=False)
        print(f"Delete response for {full_contact_url}: {del_response.status_code} - {del_response.text}")

        if del_response.status_code == 204:
            print(f"Successfully deleted: {full_contact_url}")
        else:
            print(f"Failed to delete {full_contact_url}: {del_response.status_code}")
else:
    print(f"Failed to list contacts. Status code: {response.status_code}, Response: {response.text}")
