# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

# This script is for your reference only and may not be executed succesfully.

import os

# e!COCKPIT: Create a new project
project = e_projects.create_new_project()

#e!COCKPIT: get device type from catalog
deviceTypes = e_device_catalog.find_device_type("0750-8202", "LATEST")
  
#e!COCKPIT: add an instances of the device type to the project
devices = project.add_device(deviceTypes[0], 1)
  
# e!COCKPIT: Set the IpAddress of the first device
devices[0].ip_address = "192.168.28.3"

# remove the original plc program node
plcs = project.find("PLC_PRG", True)
plcs[0].remove()

# import a new program node
applications = project.find("Application", True)
scriptDir = os.path.dirname(os.path.realpath(__file__))
importFile = os.path.join(scriptDir, "plc.xml")
applications[0].import_xml(importFile, False)

bootAppFile = os.path.join(scriptDir, "bootApp.app")

# Create a boot application (while beeing offline)
applications[0].create_boot_application(bootAppFile);
