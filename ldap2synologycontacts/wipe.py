#!/usr/bin/env python3

import requests
import xml.etree.ElementTree as ET
import urllib.parse

from config import carddav_url, carddav_username, carddav_password

response = requests.request( 
    'PROPFIND', carddav_url,
    auth=(carddav_username, carddav_password),
    headers={'Depth': 'infinity'},
    verify='synology.pem'
)

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
    # Only delete .vcf files, skipping the Administrator.vcf and collection root. This stops the whole thing from being deleted which breaks the next uploads.
        if (
            href_text.endswith('.vcf') and
            'Administrator.vcf' not in href_text
        ):
            contact_urls.append(href_text)

    if not contact_urls:
        print("No deletable contacts found.")

    for contact_url in contact_urls:
        # Use urljoin without additional quote to avoid double encoding.
        full_contact_url = urllib.parse.urljoin(carddav_url, contact_url)

        #Delete contacts
        del_response = requests.delete(full_contact_url, auth=(carddav_username, carddav_password), verify='synology.pem')
        #Log deletions
        if del_response.status_code == 200:
            print(f"Successfully deleted: {full_contact_url}")
        else:
            print(f"Failed to delete {full_contact_url}: {del_response.status_code}")
