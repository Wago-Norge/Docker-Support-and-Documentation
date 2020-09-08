# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# e!COCKPIT: Create a new project
project = e_projects.create_new_project()

# Get device type from catalog
deviceTypes = e_device_catalog.find_device_type("0750-8202", "LATEST")
# Specific verision number can also be used here:
# deviceTypes = e_device_catalog.find_device_type("0750-8202", "2.0.0.0")

# Add 2 instance of the device to the project
project.add_device(deviceTypes[0], 2)

# Get devices from primary project
devices = project.devices
print("The device count of the project now is {0}".format(devices.Count))

# Print device's GUID for each of the devices in project
for device in devices:
    print("Device guid is {0}".format(device.device_guid))

# Use first device as sample device
device = devices[0]

# Delete a device
project.delete_device(devices[1])
	
# Get devices from primary project again
devices = project.devices
print("The device count of the project now is {0}".format(devices.Count))