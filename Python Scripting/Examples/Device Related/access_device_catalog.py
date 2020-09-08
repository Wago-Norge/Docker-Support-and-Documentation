# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# get device type from catalog
deviceTypes = e_device_catalog.find_device_type("0750-8202", "LATEST")
# # A specific version can also be used like:
# deviceTypes = e_device_catalog.find_device_type("0750-8202", "LATEST")

# read some properties
for deviceType in deviceTypes:
  print("Found device type: " + str(deviceType.name) + " id: " + str(deviceType.id) + " version: " + str(deviceType.version) + " order number: " + str(deviceType.order_number) + " vendor: " + str(deviceType.vendor))