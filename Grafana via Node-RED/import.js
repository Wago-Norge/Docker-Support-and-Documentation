//Import the following JSON-text in the Node-Red:
[
    {
        "id": "5b5e5bf.50d81a4",
        "type": "influxdb out",
        "z": "65fdfaa4.31cde4",
        "influxdb": "5cec31bd.96d1f",
        "name": "Send to Influx",
        "measurement": "table01",
        "precision": "",
        "retentionPolicy": "",
        "x": 1040,
        "y": 360,
        "wires": []
    },
    {
        "id": "5cec31bd.96d1f",
        "type": "influxdb",
        "z": "",
        "hostname": "127.0.0.1",
        "port": "8086",
        "protocol": "http",
        "database": "skaugdb",
        "name": "Influxdb_Localhost",
        "usetls": false,
        "tls": ""
    }
]
