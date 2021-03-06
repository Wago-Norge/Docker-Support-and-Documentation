# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# e!COCKPIT: Create a new project
project = e_projects.create_new_project()

# print the the compiler version of the project
print("The compiler version of the project is {0}".format(project.compiler_version))

# Save the project as archive SampleSave.eca on desktop
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\SampleSave.eca')
e_projects.save_as_archive(desktop)

# Print location of archive
print("Project saved as archive: {0}".format(desktop))
