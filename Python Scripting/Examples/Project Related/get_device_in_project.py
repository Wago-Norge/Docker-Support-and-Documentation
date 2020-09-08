# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# e!COCKPIT: Create a new project
project = e_projects.create_new_project()

# get device type from catalog
deviceTypes = e_device_catalog.find_device_type("0750-8202", "LATEST")

# add 3 instances of the device type to the project
devices = project.add_device(deviceTypes[0], 3)
  
# get all devices in the project
myDevices = project.devices

# print the devices count
print(len(myDevices))
  
# get device by name
device = project.get_device("PFC200_2ETH_RS")

# print the device_guid of the device
print(device.device_guid)