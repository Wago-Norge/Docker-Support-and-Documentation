# MQTT with WAGO
This folder will contain several useful documents to help you utilize WAGO.

### Prerequisites
MQTT must be enabled in Web Based Management. Go to WBM > Cloud Connectivity and enter the necessary settings. Make sure to enable the service. Here are the settings we normally use for testing:
```
Cloud platform: MQTT AnyCloud
Clean Session: No
TLS: No
Port: 1883
Data protocol: Native MQTT
Cache mode: RAM
```
Certificates and TLS should be included for more security. 
Additionally, most IoT- and cloud platforms use TLS and port 8883 for more secure connection.

Here is an example of a PLC that is connected to Shiftr:
<div align="left">
  <img src="img\MQTT_settings.PNG" width=""><br><br>
</div>
