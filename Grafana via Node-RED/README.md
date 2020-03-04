#Using Node-RED as a gateway to InfluxDB
To use Grafana for trendning, we have to make data available to it. The easiest way to do this is currently via InfluxDB. This tutorial will explain how to create a simple gateway to InfluxDB in Node-RED. The most apparent use for this, is to send data to Node-RED from e!Cockpit, and thusly to InfluxDB via a gateway. By doing so, we can display data in Grafana. This can of course have several uses - not only displaying data from e!Cockpit, but several sources at once.

Kurt Braun has a quick guide on this here: [Youtube](https://www.youtube.com/watch?v=BBcj-ZoufMw)

###Prerequisites
This tutorial assumes that you have installed Docker and all necessary containers (Node-RED, InfluxDB and Grafana). If you have not done this, please refer to the tutorial under Installing Docker and Containers. Additionally, you can import ```import.json``` in Node-RED if you would like to skip some of the steps.
We also assume that you have some experience with JavaScript, Object-Oriented programming or Node-RED.

To send data to InfluxDB we need something/data available in Node-RED. You can either generate that in Node-RED, or you can send data from other instances. To send data, you will most likely have to communicate via the device's ethernet port. There are several ways to do this: Modbus TCP/IP, Network variables, OPC UA and MQTT are examples of such ways. Here are tutorials to do this:

[Kurt Braun: Network Variables](https://www.youtube.com/watch?v=NNqeP3N1j7E)
[Wago Norge: OPC UA](https://github.com/Wago-Norge)

More useful links will be added.
***test***
**test2**
*test3*

##InfluxDB Setup
To make data available to Grafana, we need to setup Influx. After installing InfluxDB as in our Docker tutorial, the following must be done:
 - Create a database
 - Create a measurement
The database is called 'mydb' and the measurement is called 'table01' in our tutorial.

Thereafter you can use the following commands to verify that you have a database correctly set up:
<div align="center">
   <br>
  <img src="img\Influx-shell.png"><br><br>
</div>
The database should now be reachable under localhost:8086.

##Creating a Gateway
When data is available in Node-RED, we can start on the first step: creating a gateway.
Go to your PLC's IP address, and add ```:1880```. Like ```192.168.1.17:1880```

<div align="center">
   <br>
  <img src="img\Node-RED-to-influx.png"><br><br>
</div>
In this example we have used two interval inject nodes that activates two random number generators. These are activated every 15 seconds, and have a name specified under Topic. These will serve as our data sources. The random number will be entered in msg.payload.
<div align="right">
   <br>
  <img src="img\Node-RED-inject.png"><br><br>
</div>

The Join-node will thereafter wait for a predetermined number of sourcer (here 2), and then output a list/array of every input. The output will look like this:
<div align="center">
   <br>
  <img src="img\Node-RED-influx-debug.png"><br><br>
</div>
To see how the join node is set up on our side, use ```import.json```.

The previous object is then sent to the influx node, which is setup with the correct specifications: measurement (table01), database (skaugdb) and host (```127.0.0.1:8086```).
You can now use the previous commands under the InfluxDB Setup to verify that your data is stored correctly.
...We will now visualize!

##Setting up Grafana
We can now start visualizing the available data. Go to your PLC's IP address, at port 3000. Like ```192.168.1.17:3000```.
Enter `admin` as username, and `admin` as password. Change the password as you like.

Firstly we need to add a data source. Simply choose InfluxDB, and enter the necessary data as so:
<div align="center">
   <br>
  <img src="img\Grafana-Influx-setup.png"><br><br>
</div>

###Adding a query
Thereafter, go to Dashboards. The easiest way is perhaps to press the Grafana symbol, so that you are sent back to the setup.
1. Click 'New dashboard'.
2. Click 'Add query'.
3. Select the drop down menu at 'Query'. It should say 'default' by default. Select the settings that you set up previously.
4. At FROM, click 'select measurement' and select 'table01'.
5. Click 'field(value)' and select your data. SELECT should be set to mean - but you can try other options as well.
   You should now see some datapoints or graphs appearing.
   By pressing the '+' sign, you will be able to add more fields/data sources.
6. For GROUP BY you can try other options for 'fill(...)'. This will change how the datapoints correlate.
7. Click on the side menu to add other options. Both regarding the visualization and other settings.

You can add several dashboards, which display data differently.

It is important to keep in mind with this gateway, that the messages (msg) in Node-RED should be passed on to the Influx-node in a specific way:
```
msg.payload = {
  Source 1: .............
  "Source 2": ............
  Name: ............
  123: ............
}
```
By following this template for the msg.payload, you should be able to add whichever data sources you would like, in whatever way you would like. Using the Join-node is not mandatory.


`Håkon Skaug` [Mail](mailto:hakon.skaug@wago.com)
