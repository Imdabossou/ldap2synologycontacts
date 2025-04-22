# LDAP settings
ldap_server = 'ldap://DOMAIN NAME'  # CHANGEME
ldap_username = 'CN=USERNAME,OU=SERVICEACCOUNTS,DC=AD,DC=EXAMPLE,DC=COM'  # CHANGEME
ldap_password = 'PASSWORD'  # CHANGEME
ldap_base_dn = 'CN=USERS,DC=AD,DC=EXAMPLE,DC=COM'  # CHANGEME
ldap_search_filter = '(objectClass=person)'

# CardDAV settings
carddav_url = 'https://IP ADDRESS:5001/carddav/DOMAIN@@USERNAME/123123123123123123'  # CHANGEME
carddav_username = 'USERNAME'  # CHANGEME
carddav_password = 'PASSWORD'  # CHANGEME
carddav_vcf_directory = 'vcards'