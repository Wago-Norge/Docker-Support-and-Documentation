# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# e!COCKPIT: Create a new project
project = e_projects.create_new_project()

# get device type from catalog
deviceTypes = e_device_catalog.find_device_type("0750-8202", "LATEST")
  
# add an instances of the device type to the project
devices = project.add_device(deviceTypes[0], 1)
  
# e!COCKPIT: Set the IpAddress of the first device
devices[0].ip_address = "192.168.2.201"