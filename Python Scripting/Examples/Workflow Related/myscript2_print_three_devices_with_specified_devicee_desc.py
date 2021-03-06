# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# e!COCKPIT: Create a new project
project = e_projects.create_new_project()

# print the the compiler version of the project
print("The compiler version of the project is {0}".format(project.compiler_version))

# Save the project as sample.ecp on desktop
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\e!Cpython\\MyProject.ecp')
project.save_as(desktop)

# Save project if changes was made
project.save()

deviceTypes = e_device_catalog.find_device_type("0750-8202", "LATEST")

# read some properties
for deviceType in deviceTypes:
  print("Found device type: " + str(deviceType.name) + " id: " + str(deviceType.id) + " version: " + str(deviceType.version) + " order number: " + str(deviceType.order_number) + " vendor: " + str(deviceType.vendor))