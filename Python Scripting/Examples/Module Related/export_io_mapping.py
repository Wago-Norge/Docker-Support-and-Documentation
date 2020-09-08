# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# get the folder path where the script is
scriptDir = os.path.dirname(os.path.realpath(__file__))

# get the path of the project file
projFile = os.path.join(scriptDir, "module_with_io_mapping.ecp")

# e!COCKPIT: open the project
proj = e_projects.open_project(projFile,ProjectUpdateFlag.UpdateAll)

# e!COCKPIT: get the devie in the project by name
device = proj.get_device("PFC200_G2_2ETH_RS")

# get the output path of the csv file
outputPath = os.path.join(scriptDir, "io_mapping_new.csv")

# export the io mapping of the module to the csv file
device.modules[0].export_io_mappings_as_csv(outputPath)