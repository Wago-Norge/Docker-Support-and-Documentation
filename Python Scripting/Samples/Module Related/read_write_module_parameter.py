# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

# This script is for your reference only and may not be executed succesfully.

import os

# e!COCKPIT: Create a new project
project = e_projects.create_new_project()

# get device type from catalog
deviceTypes = e_device_catalog.find_device_type("0750-8202", "LATEST")
  
# add an instances of the device type to the project
devices = project.add_device(deviceTypes[0], 1)
targetDevice = devices[0]

# e!COCKPIT: Set the IpAddress of the first device
targetDevice.ip_address = "192.168.2.201"

# add a module
moduleTypes = e_device_catalog.find_device_type("0753-0655", "LATEST")
# A specific version can also be used like:
# moduleTypes = e_device_catalog.find_device_type("0750-0523", "2.0.0.0")

# Add modules to the device
modules = targetDevice.add_module(moduleTypes[0], 0, 1)
targetModule = modules[0]

targetDevice.connect()

# Read parameter list from device and print
paramterList = targetModule.read_parameter_list()
for item in paramterList:
	print(item.Item1+":"+item.Item2)

#e!COCKPIT: read paramter with id "RootGroup"
parameterValue = targetModule.read_parameter("RootGroup")
print("parameter RootGroup before change: " + str(parameterValue))

#e!COCKPIT: write paramter with id "RootGroup"
parameterValue = targetModule.write_parameter("RootGroup", 200)

#e!COCKPIT: read paramter with id "RootGroup" again
parameterValue = targetModule.read_parameter("RootGroup")
print("parameter RootGroup after change: " + str(parameterValue))

targetDevice.disconnect()