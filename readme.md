1. ldap2vcard.py - Retrieve information from Active Directory and create them as new vCards.
2. wipe.py - Clear existing contacts from Synology contacts (apart from the contact book itself and Administrator.vcf to avoid the whole address book being deleted.)
3. sync.py - Upload contact .vcf files up to Synology contacts


sudo pacman -S python-ldap3 python-vobject python-requests

Move files into /usr/local/bin/ (requires root)

Give modify permissions to user account for ldap2synologycontacts folder in directory

Ensure run.sh is allowed to run as excecutable
Ensure each .py is allowed to run as excecutable

Move .service out into /etc/systemd/system/

sudo systemctl enable --now ldap2synologycontacts.service
