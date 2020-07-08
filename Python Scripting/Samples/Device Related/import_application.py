# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# e!COCKPIT: Create a new project
project = e_projects.create_new_project()

# get device type from catalog
deviceTypes = e_device_catalog.find_device_type("0750-8202", "LATEST")
  
# add an instances of the device type to the project
devices = project.add_device(deviceTypes[0], 3)

# get the folder path where the script is
scriptDir = os.path.dirname(os.path.realpath(__file__))

# get the path of the project file
# Native import application
nativeImportSourceFilePath = os.path.join(scriptDir, "ExportWithApplication.export")
project.import_app_native([devices[0].device_guid,devices[1].device_guid], nativeImportSourceFilePath)

# Plc Xml import application
xmlImportSourceFilePath = os.path.join(scriptDir, "ExportWithApplication.xml")
project.import_app_xml([devices[2].device_guid], xmlImportSourceFilePath)