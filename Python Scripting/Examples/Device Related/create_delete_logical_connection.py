# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# e!COCKPIT: Create a new project
project = e_projects.create_new_project()

# Get device type from catalog
deviceTypes = e_device_catalog.find_device_type("0750-8214", "LATEST")
# Specific verision number can also be used here:

# Add 6 instance of the device to the project
devices = project.add_device(deviceTypes[0], 6)

# Create logical connection: 1 -> 2
e_network.create_logical_connection(devices[0], devices[1], "canopen")

# Create logical connection: 4 -> 5
e_network.create_logical_connection(devices[3], 4, devices[4], 4, "canopen")

# Remove logical connection: 1 -> 2
e_network.delete_logical_connection(devices[0], devices[1], "canopen")

# Create logical connection: 1 -> 3
e_network.create_logical_connection(devices[0], devices[2], "canopen")

# Remove logical connection: 4 -> 5
e_network.delete_logical_connection(devices[3], 4, devices[4], 4, "canopen")

# Create logical connection: 4 -> 6
e_network.create_logical_connection(devices[3], 4, devices[5], 4, "canopen")

