# -*- coding: utf-8 -*-
# This comment is required if there are any non-ASCII characters in the script file.

import os

# e!COCKPIT: Create a new project
project = e_projects.create_new_project()

# print the the compiler version of the project
print("The compiler version of the project is {0}".format(project.compiler_version))

# Save the project as sample.ecp on desktop
#desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\e!Cpython\\MyProject.ecp')
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'C:\\scripting\\MyProject.ecp')
project.save_as(desktop)
print("Project saved...")
# Save project if changes were made
project.save()


myDevice = e_device_catalog.find_device_type("0750-8202", "LATEST")  
# add three instances of the device type to the project
devices = project.add_device(myDevice[0], 3)
print("Added 3 750-8202 with latest Firmware...")
# e!COCKPIT: Set the IpAddress for three devices
for i in range(0,3):
	devices[i].ip_address = "192.168.1." +str(i+2) # start with IP 192.168.1.2

	
# Get my project related modules
moduleDI = e_device_catalog.find_device_type("0750-1405", "LATEST")
moduleDO = e_device_catalog.find_device_type("0750-1504", "LATEST")
moduleAI_TC = e_device_catalog.find_device_type("0750-0469/0003-0000", "LATEST")
moduleAI = e_device_catalog.find_device_type("0750-0467", "LATEST")
moduleAO = e_device_catalog.find_device_type("0750-0550", "LATEST")

# assign modules to every device
for j in range(0,3):
	modules = devices[j].add_module(moduleDI[0], 0, 1)
	modules = devices[j].add_module(moduleDO[0], 1, 1)
	modules = devices[j].add_module(moduleAI_TC[0], 2, 1)
	modules = devices[j].add_module(moduleAI[0], 3, 1)
	modules = devices[j].add_module(moduleAO[0], 4, 1)
	#											 	|--Quantity	
	#											 |--Slot Index	

print("Moduleconfiguration done..")
# get the folder path where the script is
scriptDir = os.path.dirname(os.path.realpath(__file__))

# get the path of the project file
#projFile = os.path.join(scriptDir, "MyProject.ecp")

# e!COCKPIT: open the project
#proj = e_projects.open_project(projFile)

# e!COCKPIT: get the devie in the project by name


device0 = project.get_device("PFC200_2ETH_RS")
device1 = project.get_device("PFC200_2ETH_RS_1")
device2 = project.get_device("PFC200_2ETH_RS_2")

# get the path of the csv file
inputPath = os.path.join(scriptDir, "my_io_mapping.csv")

# import the io mapping of the module from the csv file
#for k in range(0,3):
device0.modules[0].import_io_mappings_from_csv(inputPath)
device1.modules[0].import_io_mappings_from_csv(inputPath)
device2.modules[0].import_io_mappings_from_csv(inputPath)	

print("Imported I/O mapping")
#----------------------------------------
project.save_as(desktop)
project.save()


#deviceConnection = e_network.create_logical_connection(devices[0],devices[1],"MODBUS_OVER_UDP")



# connect to the first 750-8202
#devices[0].connect()
#for n in range (1,3):
# connect to remaining 750-8202
#	devices[n].connect()

#-----------------------------------------------------------------------------------------------
#                                           Program Start
#-----------------------------------------------------------------------------------------------

proj = projects.primary
plcs = project.find("Application", True)
#app = plcs[1] # wich plc? --> the second "PFC200_2ETH_RS_1"
app = plcs[0] # wich plc? --> the second "PFC200_2ETH_RS"

# Create FB
myFb = app.create_pou("FbTest")

# Change declaration of the FB
implementation = myFb.textual_declaration.replace("""FUNCTION_BLOCK FbTest
VAR_INPUT
   iValue : INT;
END_VAR
VAR_OUTPUT
END_VAR
VAR
END_VAR""")

# Change implementation of the FB
myFb.textual_implementation.replace("""iValue := iValue + 1;""")

# Add method to FB
dosomething = myFb.create_method("DoSomething", "INT")

# Change declaration of the method
dosomething.textual_declaration.replace("""METHOD DoSomething : INT
VAR_INPUT
   iVal1 : INT;
   iVal2 : INT;
END_VAR""")

# Change implementation of the method
dosomething.textual_implementation.replace("""DoSomething := iVal1 + iVal2;""")

myDUT = app.create_dut("STATE", DutType.Enumeration)     # add declaration of the ENUM 
      # here parameter "DutType" can be  DutType.Structure(default), DutType.Enumeration , DutType.Alias, DutType.Union .
implementation = myDUT.textual_declaration.replace("""TYPE STATE :
(
   Examples_INT := 0,    (* *)
   SEND,      (* Send messages *)
   READ,      (* Receive messages *)
   ERROR      (* error single *)
);
END_TYPE""") 
#-----------------------------------------------------------------------------------------------
#                                          Program End
#-----------------------------------------------------------------------------------------------

# set the credentials for the device
# online.set_default_credentials("admin", "wago")

#e!COCKPIT: Connect the device(s) - Codesys and WAGO connection
devices[0].connect()

# Get the online application
app = project.active_application 
onlineapp = online.create_online_application(app)

# Create a boot application (while beeing online)


# set status of application to "run", if not in "run"
if onlineapp.is_logged_in:
    onlineapp.create_boot_application()
    if not onlineapp.application_state == ApplicationState.run:
        onlineapp.start()

	
system.delay(5000) #wait 5 sec
#e!COCKPIT: Disconnect the device(s) - Codesys and WAGO connection
devices[0].disconnect()
#
#-----------------------------------------------------------------------------------------------
#                                          Offline Bootproject
#-----------------------------------------------------------------------------------------------
#found = proj.find("Application", True)
#if not found:
#   raise Exception("Application was not found")
#app = found[0]

#app.create_boot_application("c:\scripting\myapp.app")
#-----------------------------------------------------------------------------------------------
#                                         Offline Bootproject
#-----------------------------------------------------------------------------------------------





