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

# start simulation mode
targetDevice.is_simulated = True

# start application
targetDevice.start()

# Print the current simulation status.
print(targetDevice.is_simulated)

# stop the application
targetDevice.stop()

# set the simulation mode to false
targetDevice.is_simulated = False

# Print the current simulation status.
print(targetDevice.is_simulated)