#!/usr/bin/env python3

import os
import ldap3
import vobject
import time

# LDAP server details
ldap_server = 'ldap://DOMAIN NAME'#CHANGEME
username = 'CN=USERNAME,OU=SERVICEACCOUNTS,DC=AD,DC=EXAMPLE,DC=com' #CHANGEME
password = 'PASSWORD' #CHANGEME
base_dn = 'CN=USERS,DC=AD,DC=EXAMPLE,DC=com'#CHANGEME
search_filter = '(objectClass=person)'

# Directory to store vCards
vcard_dir = 'vcards'
print(f"/{vcard_dir} set as vcard directory")

# Delete existing vcards
for filename in os.listdir(vcard_dir):
    file_path = os.path.join(vcard_dir, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
print("Directory wiped")
time.sleep(1)

# Connect to LDAP with authentication
server = ldap3.Server(ldap_server)
connection = ldap3.Connection(server, user=username, password=password, auto_bind=True)
print("Connected to LDAP")

# Search LDAP for users
connection.search(base_dn, search_filter, attributes=['cn', 'mail', 'telephoneNumber'])
print("Reading Directory")

# Create vCards
for entry in connection.entries:
    vcard = vobject.vCard()
    vcard.add('fn').value = entry.cn.value
    vcard.add('email').value = entry.mail.value if entry.mail else ''
    vcard.add('tel').value = entry.telephoneNumber.value if entry.telephoneNumber else ''
    vcard_filename = os.path.join(vcard_dir, f"{entry.cn.value}.vcf")

    # Save vCard to the specified directory
    with open(vcard_filename, "w") as vcard_file:
        vcard_file.write(vcard.serialize())
print("New vcards created")
