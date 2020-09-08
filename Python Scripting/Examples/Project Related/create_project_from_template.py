# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# Get and print available templates
templateNames = e_projects.project_template_names
for templateName in templateNames:
    print("Found template: {0}".format(templateName))

# e!COCKPIT: Create a new project from a template
project = e_projects.create_new_project_from_template("Series_750.ecp")