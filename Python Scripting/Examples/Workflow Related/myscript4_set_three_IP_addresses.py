# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# e!COCKPIT: Create a new project
project = e_projects.create_new_project()

# print the the compiler version of the project
print("The compiler version of the project is {0}".format(project.compiler_version))

# Save the project as sample.ecp on desktop
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\e!Cpython\\MyProject.ecp')
project.save_as(desktop)

# Save project if changes was made
project.save()

deviceTypes = e_device_catalog.find_device_type("0750-8202", "3.0.1.0")

# read some properties
for deviceType in deviceTypes:
  print("Found device type: " + str(deviceType.name) + " id: " + str(deviceType.id) + " version: " + str(deviceType.version) + " order number: " + str(deviceType.order_number) + " vendor: " + str(deviceType.vendor))
# get device type from catalog
deviceTypes = e_device_catalog.find_device_type("0750-8202", "LATEST")  
# add three instances of the device type to the project
devices = project.add_device(deviceTypes[0], 3)

# e!COCKPIT: Set the IpAddress for three devices
for i in range(0,3):
	devices[i].ip_address = "192.168.1." +str(i+2) #start with IP 192.168.1.2