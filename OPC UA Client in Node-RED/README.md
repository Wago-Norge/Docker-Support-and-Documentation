# Using Node-RED as a OPC UA Client
This document will explain the use of OPC UA in Node Red. The example flow that will be used here will read a virtual value off of an UaExpert Cpp demo server. The message string that is read, will then be formatted, so that it can be written to a different float variable on the OPC server hosted on the Wago PFC200.

There are several uses for OPC UA. For example sending data from the e!Cockpit environment, to

### Prerequisites
This guide assumes that an OPC server has been created on the Wago PFC. The OPC UA demo server is used to be able to read a dynamic value - but you can use any variable that you would like. Use an arbitrary OPC client/explorer (Like UaExpert) to obtain NodeIDs for the variable you want to use.


Import the JSON-file included in this folder: ```import.json```.
Set the first “Node” to contain the appropriate Node-Id of the variable that will be read.
Set the Listener node to listen on the correct server (Connector).
Server setup: Discovery and Endpoint should contain the appropriate address of the server. Should be similar to “opc.tcp://192.168.1.17:4840” if locally hosted.
Select “Auto Select Endpoint” and “Keep Session Alive”. “Endpoint Must Exist” should not be selected. Give the server an appropriate name.
The node should have “Send Just Values” selected.
<div align="center">
   <br>
  <img src="img\OPCUA_connector.png"><br><br>
</div>

Use debug node “1” to observe how the read-data is formatted. Based on this, change the “toWriteMsg” node to contain the value you want to pass in msg.payload. Playing around with this will help you understand how the strings are changed, and received.
Change the second “Node” to have the appropriate Node-Id of the variable that will be written to.
Change the last “Write” node to use the correct server. (The server that will be written to).

If the correct notation is used, the wanted value should be passed in msg.payload, and consequently appear in the OPC server. Values should always be sent through payload.


`Håkon Skaug`
