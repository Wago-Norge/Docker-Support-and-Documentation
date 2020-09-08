# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# e!COCKPIT: Create a new project
project = e_projects.create_new_project()

# get device type from catalog
deviceTypes = e_device_catalog.find_device_type("0750-8212", "LATEST")
  
# add an instances of the device type to the project
devices = project.add_device(deviceTypes[0], 1)

# add a module
moduleTypes = e_device_catalog.find_device_type("0750-0523", "LATEST")
# A specific version can also be used like:
# moduleTypes = e_device_catalog.find_device_type("0750-0523/0000-0000", "2.0.0.0")

modules = devices[0].add_module(moduleTypes[0], 0, 1)

# set io mapping
modules[0].set_io_mapping("16777216", "Kbus", "myVar2", "%IB0", "unit", "desc")