import os

project = e_projects.create_new_project()

# get device type from catalog
deviceTypes = e_device_catalog.find_device_type("0750-8202", "LATEST")

# add 2 instances of the device type to the project
devices = project.add_device(deviceTypes[0], 2)

# Create an empty POU in the added device's application
app = project.find('Application', True)
pouName = 'POU'
pou = app[0].create_pou(pouName, PouType.Program)

# Fill in the content of the created POU
pou.textual_declaration.replace("""PROGRAM %s
VAR
    i : INT;
END_VAR""" % pouName)

pou.textual_implementation.replace("""i := i + 1;""")

# Add a task which calls the created POU
found = project.find('Task Configuration', True)
print(found.Count)
if found.Count > 0:
    taskConfig = found[0]
else:
    taskConfig = app[0].create_task_configuration()
task = taskConfig.create_task('POU_Task')
task.pous.add(pouName)

# get the folder path where the script is
scriptDir = os.path.dirname(os.path.realpath(__file__))

# Native export/import
# Export the new created POU
pouNativeExportPath = os.path.join(scriptDir, "pou.export")
pou.export_native(pouNativeExportPath, True)

# Import the exported POU to the second device application
app[1].import_native(pouNativeExportPath)

# Plc Xml export/import
# create the export reporter
class expReporter(ExportReporter):
    def error(self, message):
        system.write_message(Severity.Error, message)

    def warning(self, message):
        system.write_message(Severity.Warning, message)

    def nonexportable(self):
        print("non exportable")
    
    @property
    def aborting(self):
        return False

        
pouXmlExportPath = os.path.join(scriptDir, "pou.xml")
pou.export_xml(expReporter(),pouXmlExportPath)

# create the import reporter
class impReporter(ImportReporter):
    def error(self, message):
        system.write_message(Severity.Error, message)

    def warning(self, message):
        system.write_message(Severity.Warning, message)

    def resolve_conflict(self, obj):
        return ConflictResolve.Copy

    def added(self, obj):
        print("added: ", obj)

    def replaced(self, obj):
        print("replaced: ", obj)

    def skipped(self, obj):
        print("skipped: ", obj)
    
    @property
    def aborting(self):
        return False

app[1].import_xml(impReporter(),pouXmlExportPath)