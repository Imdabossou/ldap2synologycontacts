# **LDAP2SYNOLOGYCONTACTS**

## Explanation
Problem - No solution for an iOS integrated shared syncronized global address list on an iPhone seems to exist / work.

Solution - Read contacts from LDAP, turn these into CardDAV .vcf contact files, upload them to CardDAV server, sync iPhone to CardDAV server.

The project is currently split into three separate processes for easier testing.
1. retrieve.py - Retrieve information from Active Directory and create them as new vCards.
2. wipe.py - Clear existing contacts from Synology contacts (apart from the contact book itself and Administrator.vcf to avoid the whole address book being deleted.)
3. sync.py - Upload contact .vcf files up to Synology contacts

## TO DO
Add photo field from AD.

OS independent installer & instructions. 

Upgrade process that keeps previous config.py if upgrading to a newer version.

HTTPS.


## Basic Guide

>sudo pacman -S python-ldap3 python-vobject python-requests

Move files into /usr/local/bin/ 

Give modify permissions to user account for ldap2synologycontacts folder in directory

Ensure run.sh is allowed to run as excecutable

Ensure each .py is allowed to run as excecutable

Move .service out into /etc/systemd/system/

>sudo systemctl enable --now ldap2synologycontacts.service

## DISCLAIMERS
This is specficially designed to use Synology Contacts as it is what I have available. I cannot guarantee this would work with any other CardDAV server.

This uses HTTP. Only use this on an internal network.

This currently runs on and only has instructions for Arch Linux. As it is Python it should run on just about anything, but you will need to adjust the files accordingly.

CARDDAV is not really designed to do this. It is more for individual contact books for each user.. but this is the only way I can find that integrates contacts into iOS.
The wipe.py deletes the contact list and reuploads it to reset any accidental changes by anyone. This is not a perfect solution, but the best I know of.

This is a work in progress. I am not responsible if this causes any damage, use at your own risk.

