#!/bin/bash

echo Run this script as sudo. Mark as executable with chmod +x uninstaller.sh, and run sudo ./uninstaller.sh

# Confirmation
while true; do
    read -n1 -p "Uninstall ldap2synologycontacts? (y to confirm): " answer; echo
    [[ $answer == [Yy] ]] && break
done

# Remove installed packages
sudo pacman -R python-ldap3 python-vobject python-requests
echo Packages removed

# Delete installed folder
rm -r /usr/local/bin/ldap2synologycontacts
echo Deleted ldap2synologycontacts

# Disable service
systemctl disable ldap2synologycontacts.service
echo Service disabled

# Delete service
rm /etc/systemd/system/ldap2synologycontacts.service
echo Service deleted

echo Uninstallation completed
