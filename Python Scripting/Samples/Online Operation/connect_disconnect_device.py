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
targetDevice.ip_address = "192.168.28.3"

# set the credentials for the device
online.set_default_credentials("admin", "wago")

#e!COCKPIT: Connect the device(s) - Codesys and WAGO connection
targetDevice.connect()

#e!COCKPIT: Disconnect the device(s) - Codesys and WAGO connection
targetDevice.disconnect()