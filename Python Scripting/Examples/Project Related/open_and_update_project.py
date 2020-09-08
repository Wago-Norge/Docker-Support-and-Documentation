# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# get the folder path where the script is
scriptDir = os.path.dirname(os.path.realpath(__file__))

# get the path of the project file
projFile = os.path.join(scriptDir, "project_with_old_version_settings.ecp")

# e!COCKPIT: open the project
project = e_projects.open_project(projFile)

# wait for the version change.
system.delay(1000)

# print compiler and visualization version
print("The compiler version of the project is {0} before update.".format(project.compiler_version))
print("The visualization version of the project is {0} before update.".format(project.visualization_profile))

# e!COCKPIT: open the project
project = e_projects.open_project(projFile, ProjectUpdateFlag.UpdateAll)

# wait for the version change.
system.delay(3000)

# print compiler and visualization version
print("The compiler version of the project is {0} after update.".format(project.compiler_version))
print("The visualization version of the project is {0} after update.".format(project.visualization_profile))