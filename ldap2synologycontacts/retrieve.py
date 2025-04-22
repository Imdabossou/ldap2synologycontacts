#!/usr/bin/env python3

import os
import time
import ldap3
import vobject

from .config import ldap_server, ldap_username, ldap_password, ldap_base_dn, ldap_search_filter, carddav_vcf_directory

print(f"/{carddav_vcf_directory} set as vcard directory")
for filename in os.listdir(carddav_vcf_directory):
    file_path = os.path.join(carddav_vcf_directory, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
print("Directory wiped")

time.sleep(1)

server = ldap3.Server(ldap_server)
connection = ldap3.Connection(server, user=ldap_username, password=ldap_password, auto_bind=True)
print("Connected to LDAP")
connection.search(ldap_base_dn, ldap_search_filter, attributes=['cn', 'mail', 'telephoneNumber', 'title', 'mobile'])
print("Reading Directory") 

for entry in connection.entries:
    vcard = vobject.vCard()
    vcard.add('fn').value = entry.cn.value
    vcard.add('email').value = entry.mail.value if entry.mail else ''
    tel_work = vcard.add('tel')
    tel_work.value = entry.telephoneNumber.value if entry.telephoneNumber else ''
    tel_work.type_param = 'WORK'
    tel_mobile = vcard.add('tel')
    tel_mobile.value = entry.mobile.value if entry.mobile else ''
    tel_mobile.type_param = 'CELL'
    vcard.add('title').value = entry.title.value if entry.title else ''
    vcard_filename = os.path.join(carddav_vcf_directory, f"{entry.cn.value}.vcf")
    with open(vcard_filename, "w") as vcard_file:
        vcard_file.write(vcard.serialize())
print("New vcards created")
