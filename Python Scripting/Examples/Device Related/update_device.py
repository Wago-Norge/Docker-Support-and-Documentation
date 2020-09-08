# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

# e!COCKPIT: Create a new project
e_projects.create_new_project()

# get primary project
project = e_projects.primary

# get device type from catalog
deviceTypes = e_device_catalog.find_device_type("0750-8202/0000-0011", "1.5.4.1235")

# add 1 instance of the device to the project
project.add_device(deviceTypes[0], 1)

# get devices from primary project
devices = project.devices

# Update device version to 'Latest' (or to a specific version)
devices[0].update("Latest")
# devices[0].update("1.5.7.1221")