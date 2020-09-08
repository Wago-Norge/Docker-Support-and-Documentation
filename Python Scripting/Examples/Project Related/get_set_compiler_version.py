# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# Print the latest compiler version
print("The latest compiler version is: {0}".format(e_system.latest_compiler_version))

# e!COCKPIT: Create a new project and print compiler version setting
project = e_projects.create_new_project()
print("Current project compiler version is: {0}".format(project.compiler_version))

# set the compiler_version
project.compiler_version = "3.5.11.0"

# print the compiler_version again
print("Now the project compiler version is: {0}".format(project.compiler_version))

# close e!COCKPIT
#e_system.close_e_cockpit()
