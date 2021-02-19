# Electricity Prices in Node-RED
The JSON-formatted text in `export.json` contains a demo of retrieving live electricity prices in Node-RED. This is done via Nordpool's API. 

This demo sends the data in a simple format, over OPCUA.

### Steps
- Create an array[0..23] of REAL, and publish it to OPCUA in e!Cockpit.
- Find the node-id string, and input it in the first OPCUA node.
- Receive the 24-sized array in e!Cockpit, and use it as you would like.

