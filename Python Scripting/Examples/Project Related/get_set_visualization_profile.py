# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# e!COCKPIT: Create a new project
project = e_projects.create_new_project()
print("Current visualization profile is: {0}".format(project.visualization_profile))

# set the visualization_profile
project.visualization_profile = "CODESYS V3.5 SP9 Patch 6"

# print the visualization_profile again
print("Now the visualization profile is: {0}".format(project.visualization_profile))
