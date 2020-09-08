# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

# This script is for your reference only and may not be executed succesfully.

import os

#e!COCKPIT: Create a new project
project = e_projects.create_new_project()

# get device type from catalog
deviceTypes = e_device_catalog.find_device_type("0750-8202", "LATEST")
  
#e!COCKPIT:  add an instances of the device type to the project
devices = project.add_device(deviceTypes[0], 1)
targetDevice = devices[0]

# e!COCKPIT: Set the IpAddress of the first device
targetDevice.ip_address = "192.168.3.72"

# remove the original plc program node
plcs = project.find("PLC_PRG", True)
plcs[0].remove()

# import a new program node
applications = project.find("Application", True)
scriptDir = os.path.dirname(os.path.realpath(__file__))
importFile = os.path.join(scriptDir, "plc.xml")
applications[0].import_xml(importFile, False)

# set the credentials for the device
online.set_default_credentials("admin", "wago")

#e!COCKPIT: Connect the device(s) - Codesys and WAGO connection
targetDevice.connect()

# Get the online application
app = project.active_application 
onlineapp = online.create_online_application(app)

# Create a boot application (while beeing online)
onlineapp.create_boot_application();

# starts the application on the device
targetDevice.start()

system.delay(10000)
	
# Read value of parameters:
result = onlineapp.read_value("PLC_PRG.i")	
print("Current value of i:" + result)

#e!COCKPIT: Disconnect the device(s) - Codesys and WAGO connection
targetDevice.disconnect()