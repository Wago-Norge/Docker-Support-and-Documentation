# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# get the folder path where the script is
scriptDir = os.path.dirname(os.path.realpath(__file__))

# get the path of the project file
projFile = os.path.join(scriptDir, "project_with_old_version_settings.ecp")

# e!COCKPIT: open the project
project = e_projects.open_project(projFile)

# print compiler and visualization version
print("The compiler version of the project is {0} before updating devices.".format(project.compiler_version))
print("The visualization version of the project is {0} before updating devices.".format(project.visualization_profile))

# update all the devices in the project
project.update(ProjectUpdateFlag.DeviceVersions)

# print compiler and visualization version
print("The compiler version of the project is {0} after updating devices.".format(project.compiler_version))
print("The visualization version of the project is {0} after updating devices.".format(project.visualization_profile))

# update the settings in the project
project.update()

# print compiler and visualization version again
print("The compiler version of the project is {0} after updating".format(e_projects.primary.compiler_version))
print("The visualization version of the project is {0} after updating".format(project.visualization_profile))