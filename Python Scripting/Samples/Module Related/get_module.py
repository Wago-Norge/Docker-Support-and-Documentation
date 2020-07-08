# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

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
moduleTypes = e_device_catalog.find_device_type("0750-0523", "LATEST")
# A specific version can also be used like:
# moduleTypes = e_device_catalog.find_device_type("0750-0523", "2.0.0.0")

modules = targetDevice.add_module(moduleTypes[0], 0, 2)

# Get module from a device using module name
module = targetDevice.get_module("_1RO_230_VAC_16A_Pot_free_Relay1NO")
# Print module's guid
print(module.module_guid)

# Get all modules in device
allModules = targetDevice.modules
for module in allModules:
	print(module.module_guid)