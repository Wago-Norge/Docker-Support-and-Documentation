/*
Example application for communication between the Node-Red interface and PFC200 via OPC UA. 
The application pulls weather data from YR.no, and writes the formatted data to a PLC.


Import the following JSON-text in the Node-Red: */

[
    {
        "id": "8598d743.95b748",
        "type": "tab",
        "label": "OPC UA: Read to Write",
        "disabled": false,
        "info": ""
    },
    {
        "id": "a1f644d2.694e58",
        "type": "OPCUA-IIoT-Node",
        "z": "8598d743.95b748",
        "injectType": "listen",
        "nodeId": "ns=3;s=AirConditioner_1.Temperature",
        "datatype": "NodeId",
        "value": "",
        "name": "",
        "topic": "",
        "showErrors": false,
        "x": 390,
        "y": 460,
        "wires": [
            [
                "18bc7472.92dbcc"
            ]
        ]
    },
    {
        "id": "18bc7472.92dbcc",
        "type": "OPCUA-IIoT-Listener",
        "z": "8598d743.95b748",
        "connector": "496c6e46.152ef",
        "action": "subscribe",
        "queueSize": 10,
        "name": "",
        "topic": "",
        "justValue": true,
        "useGroupItems": false,
        "showStatusActivities": false,
        "showErrors": false,
        "x": 540,
        "y": 460,
        "wires": [
            [
                "73adb976.179ce8",
                "3d0ed795.8ce718"
            ]
        ]
    },
    {
        "id": "d1d40cd1.6aed9",
        "type": "inject",
        "z": "8598d743.95b748",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 240,
        "y": 460,
        "wires": [
            [
                "a1f644d2.694e58"
            ]
        ]
    },
    {
        "id": "73adb976.179ce8",
        "type": "debug",
        "z": "8598d743.95b748",
        "name": "1",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "true",
        "targetType": "full",
        "x": 710,
        "y": 400,
        "wires": []
    },
    {
        "id": "20d3f706.335308",
        "type": "OPCUA-IIoT-Node",
        "z": "8598d743.95b748",
        "injectType": "write",
        "nodeId": "ns=4;s=|var|WAGO 750-8212 PFC200 G2 2ETH RS.Application.GVL.testNum",
        "datatype": "Float",
        "value": "",
        "name": "",
        "topic": "",
        "showErrors": false,
        "x": 750,
        "y": 660,
        "wires": [
            [
                "b2492786.88a348",
                "51879e06.a26be"
            ]
        ]
    },
    {
        "id": "51879e06.a26be",
        "type": "OPCUA-IIoT-Write",
        "z": "8598d743.95b748",
        "connector": "819fec9b.54c7f",
        "name": "",
        "justValue": false,
        "showStatusActivities": false,
        "showErrors": true,
        "x": 910,
        "y": 660,
        "wires": [
            [
                "4523714e.964e9"
            ]
        ]
    },
    {
        "id": "b2492786.88a348",
        "type": "debug",
        "z": "8598d743.95b748",
        "name": "2",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "true",
        "targetType": "full",
        "x": 910,
        "y": 620,
        "wires": []
    },
    {
        "id": "4523714e.964e9",
        "type": "debug",
        "z": "8598d743.95b748",
        "name": "3",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "true",
        "targetType": "full",
        "x": 1070,
        "y": 660,
        "wires": []
    },
    {
        "id": "3d0ed795.8ce718",
        "type": "function",
        "z": "8598d743.95b748",
        "name": "toWriteMsg",
        "func": "//This function formats the msg object to only contain the id, payload and an empty topic. \n\nmsg = { \"_msgid\": msg._msgid, \n        \"payload\": msg.payload.value.value, //This notation may vary. Use Node 1 to find the notation for the specific value that you're after.\n                                            //You could also just write \"payload\": true, 5, 5.0, or \"5\"\n        \"topic\": \"\"};\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 730,
        "y": 460,
        "wires": [
            [
                "20d3f706.335308"
            ]
        ]
    },
    {
        "id": "8dec73eb.f5e5e",
        "type": "comment",
        "z": "8598d743.95b748",
        "name": "Use this node to understand the format we recieve from OPC UA",
        "info": "",
        "x": 1030,
        "y": 400,
        "wires": []
    },
    {
        "id": "d92c2ad3.c481c8",
        "type": "comment",
        "z": "8598d743.95b748",
        "name": "Use this node to format the msg object",
        "info": "",
        "x": 1010,
        "y": 460,
        "wires": []
    },
    {
        "id": "69b1127b.79110c",
        "type": "comment",
        "z": "8598d743.95b748",
        "name": "Click here for information",
        "info": "This flow recieves a temperature from a CPP OPC UA demo server. It then formats the JSON-string, to wash away unecessary gibberish, and also to see what kind of msg object the write-node requires to do its job. In this case, using a msg object with an ID, a payload and an empty topic has worked. \n\nThe payload is msg.payload.value.value in this case, but may vary upon the object it recieves. If your value is msg.payload.random, you should replace it with this.",
        "x": 270,
        "y": 400,
        "wires": []
    },
    {
        "id": "a8a60a30.ce2f88",
        "type": "comment",
        "z": "8598d743.95b748",
        "name": "Håkon @ Wago",
        "info": "",
        "x": 1100,
        "y": 720,
        "wires": []
    },
    {
        "id": "496c6e46.152ef",
        "type": "OPCUA-IIoT-Connector",
        "z": "",
        "discoveryUrl": "opc.tcp://192.168.1.50:48010",
        "endpoint": "opc.tcp://192.168.1.50:48010",
        "keepSessionAlive": true,
        "loginEnabled": false,
        "securityPolicy": "None",
        "securityMode": "NONE",
        "name": "UaServerCpp",
        "showErrors": false,
        "individualCerts": false,
        "publicCertificateFile": "",
        "privateKeyFile": "",
        "defaultSecureTokenLifetime": "",
        "endpointMustExist": false,
        "autoSelectRightEndpoint": true,
        "strategyMaxRetry": "",
        "strategyInitialDelay": "",
        "strategyMaxDelay": "",
        "strategyRandomisationFactor": "",
        "requestedSessionTimeout": "",
        "connectionStartDelay": "",
        "reconnectDelay": "",
        "maxBadSessionRequests": "10"
    },
    {
        "id": "819fec9b.54c7f",
        "type": "OPCUA-IIoT-Connector",
        "z": "",
        "discoveryUrl": "opc.tcp://192.168.1.17:4840",
        "endpoint": "opc.tcp://192.168.1.17:4840",
        "keepSessionAlive": true,
        "loginEnabled": false,
        "securityPolicy": "None",
        "securityMode": "NONE",
        "name": "OPCUAServer@PFC200V3-44FA70",
        "showErrors": false,
        "individualCerts": false,
        "publicCertificateFile": "",
        "privateKeyFile": "",
        "defaultSecureTokenLifetime": "",
        "endpointMustExist": false,
        "autoSelectRightEndpoint": true,
        "strategyMaxRetry": "",
        "strategyInitialDelay": "",
        "strategyMaxDelay": "",
        "strategyRandomisationFactor": "",
        "requestedSessionTimeout": "",
        "connectionStartDelay": "",
        "reconnectDelay": "",
        "maxBadSessionRequests": "10"
    }
]
