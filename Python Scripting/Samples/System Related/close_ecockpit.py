# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# Get and print e!COCKPIT latest compiler version
print("e!COCKPIT latest compiler version: {0}".format(e_system.latest_compiler_version))

# e!COCKPIT: Create a new project from a template
project = e_projects.create_new_project()

# Close e!COCKPIT
e_system.close_e_cockpit()

