# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# e!COCKPIT: Create a new project
project = e_projects.create_new_project()

# print the the compiler version of the project
print("The compiler version of the project is {0}".format(project.compiler_version))

# Save the project as sample.ecp on desktop
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\e!Cpython\\MyProject.ecp')
project.save_as(desktop)

# Save project if changes was made
project.save()


myDevice = e_device_catalog.find_device_type("0750-8202", "LATEST")  
# add three instances of the device type to the project
devices = project.add_device(myDevice[0], 3)

# e!COCKPIT: Set the IpAddress for three devices
for i in range(0,3):
	devices[i].ip_address = "192.168.1." +str(i+2) # start with IP 192.168.1.2

	
# moduleTypes = e_device_catalog.find_device_type("0750-1405", "LATEST")
# modules = devices[0].add_module(moduleTypes[0], 0, 1)

# moduleTypes = e_device_catalog.find_device_type("0750-1505", "LATEST")
# modules = devices[0].add_module(moduleTypes[0], 1, 1)

moduleDI = e_device_catalog.find_device_type("0750-1405", "LATEST")
moduleDO = e_device_catalog.find_device_type("0750-1505", "LATEST")
moduleAI_TC = e_device_catalog.find_device_type("0750-0469/0003-0000", "LATEST")
moduleAI = e_device_catalog.find_device_type("0750-0467", "LATEST")
moduleAO = e_device_catalog.find_device_type("0750-0550", "LATEST")

modules = devices[0].add_module(moduleDI[0], 0, 1)
modules = devices[0].add_module(moduleDO[0], 1, 1)
modules = devices[0].add_module(moduleAI_TC[0], 2, 1)
modules = devices[0].add_module(moduleAI[0], 3, 1)
modules = devices[0].add_module(moduleAO[0], 4, 1)
		
modules = devices[1].add_module(moduleDI[0], 0, 1)
modules = devices[1].add_module(moduleDO[0], 1, 1)
modules = devices[1].add_module(moduleAI_TC[0], 2, 1)
modules = devices[1].add_module(moduleAI[0], 3, 1
modules = devices[1].add_module(moduleAO[0], 4, 1)

modules = devices[2].add_module(moduleDI[0], 0, 1)
modules = devices[2].add_module(moduleDO[0], 1, 1)
modules = devices[2].add_module(moduleAI_TC[0], 2, 1)
modules = devices[2].add_module(moduleAI[0], 3, 1
modules = devices[2].add_module(moduleAO[0], 4, 1)