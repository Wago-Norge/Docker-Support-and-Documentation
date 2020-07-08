# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# get the folder path where the script is
scriptDir = os.path.dirname(os.path.realpath(__file__))

# get the path of the project file
projFile = os.path.join(scriptDir, "module_without_io_mapping.ecp")

# e!COCKPIT: open the project
proj = e_projects.open_project(projFile,ProjectUpdateFlag.UpdateAll)

# e!COCKPIT: get the devie in the project by name
device = proj.get_device("PFC200_G2_2ETH_RS")

# get the path of the csv file
inputPath = os.path.join(scriptDir, "io_mapping.csv")

# import the io mapping of the module from the csv file
device.modules[0].import_io_mappings_from_csv(inputPath)