# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# get the folder path where the script is
scriptDir = os.path.dirname(os.path.realpath(__file__))

# get the path of the archive file
archiveFile = os.path.join(scriptDir, "eC_archive.eca")

# open archive file
project = e_projects.open_archive(archiveFile)
