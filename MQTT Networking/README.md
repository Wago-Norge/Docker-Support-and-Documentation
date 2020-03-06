# A Simple Network Application With Multiple PLC Agents

### About the application
This is a simple application where MQTT is used to communicate between two PLC's through an online broker. One node will act as a publisher, and the second will subscribe to the topic. Afterwards, Node-RED, InfluxDB and Grafana will be used to visualize. For a more thorough guide on the second subject, refer to our other guide [Grafana via Node-RED](https://github.com/Wago-Norge/Docker-Support-and-Documentation/tree/master/Grafana%20via%20Node-RED).

### Prerequesites
A Wago PFC200, or two, is required to set up the MQTT networking, as well as an internet connection. The walkthrough will later require that Node-RED, InfluxDB and Grafana are installed in Docker on a Wago PFC200 Gen 2. This can be done by following the instructions in our guide: [Installing Docker](https://github.com/Wago-Norge/Docker-Support-and-Documentation/tree/master/Installing%20Docker).

The later part of this walkthrough does not require advanced skills in Node-RED, but some experience may be good to have. See our beginner guide to Node-RED [here](https://github.com/Wago-Norge/Docker-Support-and-Documentation/tree/master/Node-RED-Tutorial)

## Setting up the MQTT broker

In order to communicate on the network we will need a broker. There are many ways of doing that, and we will use a straight forward website called [shiftr.io](https://shiftr.io). After signing up and making the MQTT broker, we connect the broker to the PLC via Wago's WBM

<div align="left">
  <img src="img\user_password_broker.png" width=""><br><br>
</div>

One can find the username and password before the @, separated by a ":". This should be added like shown below

<div align="left">
  <img src="img\WBM_Shiftr_setup.PNG" width=""><br><br>
</div>

Recall that the changes won't take affect before the Submit button is used. In our application, one of our 3 PLC's are publishing (MyCounter), and the two others are subscribing to the topic which is published on. Below is our quick setup on the PLC, see the [src](https://github.com/Wago-Norge/Simple-PLC-MQTT-Networking/tree/master/src) folder for e!C file.

<div align="left">
  <img src="img\ecockpit-code-setup.PNG" width=""><br><br>
</div>

#### Counter and Topic
After setting up the PLC and Shiftr, the counter from PLC-200-80 is displayed in the top left corner, as seen in the picture below.
<div align="left">
  <img src="img\MyCounter-shiftr.PNG" width=""><br><br>
</div>

Here we also see the topic `v1/devices/me/telemetry`. The counter is continuously updated as the PLC is constantly counting up the variable. We will present it graphically in Grafana using an Influx dataBase.

<br></br>


## Setting up InfluxDB
To make the setup possible, we need to assign a database and equip it up with a measurement, a field key, and a tag key. After logging in to the PLC with an SSH tool, we start the setup by running InfluxDB with the command

```docker exec -it influx influx```

Then we can create a database and make a measurement within that database
```hack
> create database myCounterDB
> use myCounterDB
> insert table01,status=counting MyCounter=23
> show measurements
```

And hence you should get

<div align="left">
  <img src="img\show_measurements.PNG" width=""><br><br>
</div>

where we see that table01 is the only measurement. In the commands above, we created table01 with the **tag key** `status`, and the **tag key value** `counting`.\
Additionally we created the **field key** `MyCounter` with the **field key value** `23`, which made `MyCounter` automatically be a float.

We can check this by running the command `show field keys`

<div align="left">
  <img src="img\show_field_keys.PNG" width=""><br><br>
</div>

Where we see that MyCounter is a float.\
Furthermore, we can directly inspect MyCounter's value by running the command `select last(MyCounter), * from table01` which gives us

<div align="left">
  <img src="img\select_from_MyCounter.PNG" width=""><br><br>
</div>

Where we see that `MyCounter` is 23, with the tag key value `counting`. We can also see the time stamp for the data insertion. It is possible at this point to also run the command `select * from table01` which gives

<div align="left">
  <img src="img\select_all_from_MyCounter.PNG" width=""><br><br>
</div>

but this command is not recommended to use, since it displays absolutely all data in table01, and later on in our example, every count would be registered as a separate data entry, thus you would try to list several millions of entries, by increasing timestamps, meaning you will not see the latest data entries, and there will be too many to display.



So now we are all set with the database. It contains the measurement table01 with our field key `Mycounter` and the initial value `23`. We will use this field key in Node-Red to store our counting.
<br><br>

## Implementation in Node-Red

As configured in the [Installing Docker](https://github.com/Wago-Norge/Docker-Support-and-Documentation/tree/master/Installing%20Docker) guide, one can access Node-Red by logging in to the website 192.168.x.yz:1880, where x,y,z depends on the IP address you have assigned the PLC.
Here we have made the following flow

<div align="center">
    <br>
  <img src="img\node-red-mqtt.PNG" width=""><br><br>
</div>

We have added

- A compose block containing a small Javascript code.
- An influxDB output block that will write values to an InfluxDB measurement.
- A debug flow to log what is happening.
- Simple MQTT Communication. This communication is set up identically on three different PLC's.

<br></br>


##### MQTT Node
The MQTT node is quickly up and running just by adding the appropriate topic

<div align="center">
    <br>
  <img src="img\mqtt_out_node.PNG" width="500"><br><br>
</div>

<br></br>

##### Javascript function flow
The function nodes "compose", run on Javascript-code. Here the counter is being parsed from the payload array at position 0 into MyCounter, and the whole message is returned as the output.  


```javascript
msg.payload = {
    MyCounter: parseFloat(msg.payload[0]),
    }
return msg;
```

<br></br>

##### InfluxDB output flow
Finally the message is stored in a measurement in the influx database. All that is needed in this flow is to pass the message to a valid measurement that is created through InfluxDB. In this case we configured it to table01 in the myCounterDB

<div align="left">
    <br>
  <img src="img\node-red-influx_2.PNG" width="370"> <img src="img\node-red-influx_1.PNG" width="410"><br><br>
</div>

Here is the InfluxDB flow config. The server is set to one of the PLC's IP-addresses on the default InfluxDB port 8086. Measurement has to be a valid measurement created in influx.

<br></br>


##### Shiftr.io

When all this is done, we can log in on shiftr and see the setup visualized. It should look something like this

<div align="left">
  <img src="img\mqtt-shiftr.PNG" width=""><br><br>
</div>

<br></br>



## Using Graphana
Lastly we will graphically show the counter in Grafana. Log on to the website 192.168.x.yz:3000, where x,y,z depends on the IP address you have assigned the PLC. There you will be requested to make a password, and the default login is `admin / admin`.
Then add InfluxDB as the data source and set up a new dashboard. How to do this can easily be found in several [video tutorials](https://youtu.be/JdV4x925au0) online.

For our implementation, we connected the database with Grafana in the following way


<div align="center">
    <br>
  <img src="img\graphana-config.PNG" width="700"><br><br>
</div>

By adding a new graph and displaying a query from InfluxDB, we find MyCounter stored under table01. Furthermore, we configured the graph to display the mean of the value. Hence MyCounter, sent from the PLC, will be graphically shown as

<div align="center">
    <br>
  <img src="img\graphana-graph.PNG" width=""><br><br>
</div>

where we see that MyCounter is just increasing linear, as expected, since it is constantly counting.

<br></br>

So there you have it, an easy quick use of docker, using InfluxDB, Node-Red and Grafana, all together on Wago PLC's through an MQTT broker. Feel free to reach out and inquire about *your* docker application ideas. You can find our contact information for technical support [here](https://github.com/Wago-Norge/Docker-Support-and-Documentation/) and general order inquiries [here](https://www.wago.com/no/kontaktpersoner).
