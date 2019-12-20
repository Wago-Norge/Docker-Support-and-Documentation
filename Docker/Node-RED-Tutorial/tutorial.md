# Node-RED Tutorial
If anything is unclear, please do not hesitate to contact me at [hakon.skaug@wago.com](mailto:hakon.skaug@wago.com)

“Node-RED is a programming tool for wiring together hardware devices, APIs and online services in new and interesting ways.” (www.nodered.org)
Node-RED is special because it is, unlike other ways of programming, a more visual way of programming and knitting together different services.
It clearly visualizes the flow of a program, and passes objects between the different nodes, to transport data.

With Node-RED, a PLC can easily be connected to smarter services that aren’t available in traditional developer environments.
For instance, the Google API, or YR XML weather forecast.

This guide will show how Node-RED is installed with Docker, and introduce you to simple steps for programming.
This guide assumes that you have already installed the latest firmware on your PLC, and the Docker.ipk.

### First off:
1.  Connect to your PLC through PuTTY (or a different SSH terminal).
    Address: IP of your PLC
    User: root
    Password: wago (this can be changed)
2.  To see the different docker commands, type “docker”. Entering a command, and thereafter “--help” will display options.
    For instance: “docker --help”. You can also try "docker container --help".

### Installing Node-RED
1.  Download Node-RED
    Type ```docker pull wagoautomation/node-red-iot```. This will download Wago's Node-RED image from the Docker Hub.
    Wago’s images can be found here: https://hub.docker.com/u/wagoautomation
    When this is done, you can type ```docker images``` to display the images installed on this device.
<div align="center">
   <br>
  <img src="img\docker_container.png"><br><br>
</div>

2.  Run/Install Node-RED
    The downloaded image will now be run as a container. The run command can be entered with many different options. For this example, we want to use:
    ```
    docker run -p 1880:1880 --network host --restart always --name nodered wagoautomation/node-red-iot
    ```
    The options that are used with this command will publish Node-RED at port 1880, and make sure that the container restarts if the PLC would shut down.
    There are also other useful options, like saving the flows outside of the container on a seperate volume, for instance.

    When this is done, type ```docker container ls``` or ```docker ps``` to display all running containers.
<div align="center">
   <br>
  <img src="img\docker_container_1.png"><br><br>
</div>

3.  Enter the Node-RED editor
    Enter the editor by entering the PLC’s ip-address and port 1880, like:
    `192.168.1.17:1880`

    The editor should look like this:
<div align="center">
    <br>
  <img src="img\node_red1.png"><br><br>
</div>

The editor consists of the nodes (to the left), the flow (in the middle) and the sidebar (to the right). The menu at the top right can be used to display
the sidebar (Meny > View > Sidebar), if it doesn’t show already. The debug page (insect) is key. This is where feedback from debug nodes will be printed.
You can use this to observe how data flows through the different nodes:

Insert an inject node, and then send it to a debug node. You will then observe the msg object in the debug field:
<div align="center">
    <br>
  <img src="img\node_red2.png"><br><br>
</div>

The debug node that is used here, prints the “whole” msg object. Not just msg.payload. Keep in mind that you can alter this object, or create your own -
but Node-RED relies on objects being passed between the nodes. To learn more, try using: “function” or “change” to change the msg, or its values.

Important: Keep in mind that values should be passed in the msg.payload attribute. Later, when we will try passing messages through OPCUA, modbus, or other
means of communicating, the value we want to send will lie here.


You should now have the necessary tools to start using Node-RED. Below, examples will follow.

### Gathering weather data
There are several ways to gather weather data. In this example, a HTTP request will be used. This is a service that is available in CoDeSys and e!Cockpit,
but the data is easier to process in Node-RED.


1.  Find an appropriate forecast, and its’ URL:
We will be using: https://www.yr.no/sted/Norge/Oslo/Oslo/Oslo/varsel_time_for_time.xml in this example - a forecast that provides us with data for each hour
in Oslo, for the next 24 hours.

2.  Integrate the http request into the flow:
First, we need an inject node to activate/pull the request.
Second, we need an http node where we specify what we want to pull.
Thirdly, we need an XML node that converts the data from XML to JSON. These are just different ways of representing the data on. To see how the data looks
like in XML, click the link in step 1. At the end, we should apply a debug node, so that we can observe the data.
<div align="center">
    <br>
  <img src="img\node_red3.png"><br><br>
</div>

The data will end up as a parsed JSON string. We can use dot-notation or array-notation to retrieve the data we want.

For instance, if we want to find out for what city this forecast is, we can get it by retrieving: msg.payload.weatherdata[0].name[0]
The actual weather data is usually stored in msg.payload.forecast.tabular[0].....


3.  Create a filter to retrieve selected data:
As is, the data is a large XML- or JSON string. To use the data we receive, we should cut away the info we do not need. Storing the interesting data in new
variables is preferable.

There are many ways to Rome - but one way to select the specific data we want, is by using the function node. This node takes a msg object in, and returns a
msg object. It can however modify the object, and more, based on the msg. Here, we can use classic OOP-programming - a safe haven if Node-RED sometimes confuses you.
<div align="center">
    <br>
  <img src="img\node_red4.png"><br><br>
</div>

4.  Debug
Above is the function node, with the name “filter”. To help debug your application, you can use different debug nodes with different names. To the right,
you can observe the same message (collapsed) appearing, but from different nodes. As soon as we alter the msg in the filter node, you will see a different
msg appear, with other values. Below is the message expanded.
<div align="center">
    <br>
  <img src="img\node_red5.png"><br><br>
</div>

5.  Write code:
We could for instance use the filter to retrieve weather data from between 17:00 and 18:00, later today. The area to the left, is where we program the filter node.
By using observing the expanded message to the right, we can find the correct notation to retrieve the data we want.
We then reformat msg.payload, to only contain the three values. We could also just say msg.payload = 13; if we wanted - it does not have to be a list.
The result is two msg objects that are very similar, except that their payloads vary:
<div align="center">
    <br>
  <img src="img\node_red5.png"><br><br>
</div>

With this, we could easily pass specific values, for specific times, onwards. The values can instantly be sent to the PLCs’ environment e!Cockpit, or we could use
them with logic in Node-RED. Node-RED can be easier to use, with regards to object-oriented programming, but e!Cockpit is more reliable when it comes to controlling.
