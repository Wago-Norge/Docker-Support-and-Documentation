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

# Add two modules to the device
modules = targetDevice.add_module(moduleTypes[0], 0, 2)

# Delete one of the modules from the device
targetDevice.delete_module(modules[0])