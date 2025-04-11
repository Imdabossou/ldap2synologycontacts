#!/usr/bin/env python3
import os
import ldap3
import vobject
import time

ldap_server = 'ldap://DOMAIN NAME'#CHANGEME
username = 'CN=USERNAME,OU=SERVICEACCOUNTS,DC=AD,DC=EXAMPLE,DC=COM' #CHANGEME
password = 'PASSWORD' #CHANGEME
base_dn = 'CN=USERS,DC=AD,DC=EXAMPLE,DC=COM'#CHANGEME
search_filter = '(objectClass=person)'

vcard_dir = 'vcards'
print(f"/{vcard_dir} set as vcard directory")
for filename in os.listdir(vcard_dir):
    file_path = os.path.join(vcard_dir, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
print("Directory wiped")
time.sleep(1)

server = ldap3.Server(ldap_server)
connection = ldap3.Connection(server, user=username, password=password, auto_bind=True)
print("Connected to LDAP")
connection.search(base_dn, search_filter, attributes=['cn', 'mail', 'telephoneNumber', 'title', 'mobile'])
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
    vcard_filename = os.path.join(vcard_dir, f"{entry.cn.value}.vcf")
    with open(vcard_filename, "w") as vcard_file:
        vcard_file.write(vcard.serialize())
print("New vcards created")
