#!/usr/bin/python

import requests
import json

inventory_file_url = 'https://github.com/CJJM/ansible_dynamic_inventory/blob/master/inventory-source.json'
r = requests.get(inventory_file_url)
print r.text
