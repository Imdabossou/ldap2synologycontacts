#!/bin/bash

cd /usr/local/bin/ldap2synologycontacts/

while true; do
  ./retrieve.py
  ./wipe.py
  ./sync.py
  sleep 1h
done
