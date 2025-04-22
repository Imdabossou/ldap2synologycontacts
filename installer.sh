#!/bin/bash

echo Run this script as sudo. Mark as executable with chmod +x installer.sh, and run sudo ./installer.sh

# Confirmation
while true; do
    read -n1 -p "Install ldap2synologycontacts? (y to confirm): " answer; echo
    [[ $answer == [Yy] ]] && break
done

# Install required packages (system wide)
sudo pacman -S --needed python-ldap3 python-vobject python-requests

# Create vcards directory
mkdir -p ldap2synologycontacts/vcards

# Move folder to /usr/local/bin
cp -r ldap2synologycontacts/ /usr/local/bin/

# Set permissions on folder
chmod -R o+rw /usr/local/bin/ldap2synologycontacts/

# Mark processes as executable
chmod +x /usr/local/bin/ldap2synologycontacts/retrieve.py
chmod +x /usr/local/bin/ldap2synologycontacts/wipe.py
chmod +x /usr/local/bin/ldap2synologycontacts/sync.py
chmod +x /usr/local/bin/ldap2synologycontacts/run.sh

# Move service to systemd
mv /usr/local/bin/ldap2synologycontacts/ldap2synologycontacts.service /etc/systemd/system

# Enable service but don't start yet incase configuration has not been done
systemctl enable ldap2synologycontacts.service
echo Please ensure configuration has been completed in .py files before starting service

# Start service now?
while true; do
    read -n1 -p "Start service now? (y to confirm, n to cancel): " answer; echo
    if [[ $answer == [Yy] ]]; then
        systemctl start ldap2synologycontacts.service
        echo Service started
        break
    elif [[ $answer == [Nn] ]]; then
        exit 1
    fi
done

echo Installation completed


