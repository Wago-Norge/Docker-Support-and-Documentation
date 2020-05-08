
# Docker Support

> If you are a developer or an experienced user and you want exploit the equipments capailities to the fullest, then the new PLC's from Wago is the perfect thing for you. Here we have "unlocked" the PLC's and made the source code open source with a dedicated [firmware SDK](https://github.com/WAGO/pfc-firmware-sdk). This gives unknown possibilities and ties together the atuomation-, and softwareworld. One of our newest PLC's PFC200 G2, supports [Docker](https://www.docker.com/why-docker), which is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and ship it all out as one package. Hence Docker is a great tool for developers, and that brings us to this repository, which is a thourough guide on how to set up your PLC with Docker.


## Prerequesties

The following steps must be completed in order to install a Docker Runtime Environment on a Wago PFC200 Generation 2 (e.g. 750-82xx, where xx > 11):

- The firmware of the PLC must be of version 12 or newer. Check this in the **Information** tab in the WBM (Web Based Management). \
If it is below 12, follow the firmware update instructions provided [here](https://github.com/Wago-Norge/Wago-Fastvare-Oppdatering).
Subsequently, the new firmware should be copied to the internal flash memory.

- In order to get a certificate based communication to work, set the correct time and date on the PLC in the WBM tab **Clock**.

- Make sure the PLC has online internet access, such that it can load docker images.

- Enter an available DNS server.

- Download [Docker Community Edition](https://github.com/WAGO/docker-ipk/releases), provided by Wago as a statically linked binary file packed in linux .ipk format.

- Make sure your computer has an SSH Client, for example [Putty](https://www.putty.org).





----------------------------------------------------------------------------------------



## Installation

1. Start the Wago PLC


2. Navigate to the tab **Software Uploads** in the WBM
<div align="center">
  <img src="img\install_docker_ipk.png" >
</div>


3. Find the docker .ipk file in your file system (e.g. docker_xx.xx.xx_armhf.ipk) and upload it to the PLC


4. Stand up and shout loud to the PLC "I am the master, you are the slave!"


5. After finishing the upload process, press the **Submit** button to activate the software package


6. Ignore possible error messages like
<div align="center">
  <img src="img\error_while_activationg.png" >
</div>


7. In the WBM, navigate to **Networking -> Routing** and activate the IP Forwarding chekbox. **Don't forget to press the Submit button!**
<div align="center">
  <img src="img\ipforwarding.png" >
</div>


8. Navigate to **Administration -> Reboot** and restart the PLC


9. After successful reboot, login to the PLC via the SSH Client with `login / password = root / wago`


10. Check the docker installation with the commands
```hack
docker info   # to display system-wide information
docker ps     # to list running containers (no containers should run)
docker images # to list all preinstalled images
 ```
If all is good, then you are done. You can find a list of more Docker commands [here](https://docs.docker.com/engine/reference/commandline/docker/).

#### Known issues
For a properly functioning [Docker bridge network](https://youtu.be/Js_140tDlVI), the firewall has to be disabled. If you can't disable the firewall, use the [docker overlay](https://docs.docker.com/network/overlay/) or [macvlan network](https://docs.docker.com/network/macvlan/) drivers.





----------------------------------------------------------------------------------------
## Some common Containers

Below are some commands you can run in order to install some common containers.


```
docker pull portainer/portainer
docker volume create portainer_data
docker run  -d -p 9000:9000 --network host --restart always --name portainer -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
```


```
docker pull wagoautomation/node-red-iot
docker run -p 1880:1880 --network host --restart always --name nodered wagoautomation/node-red-iot
```


```
docker pull grafana/grafana
docker run -d --name=grafana -p 3000:3000 --network host --restart always grafana/grafana
```


```
docker pull influxdb
docker volume create influx_data
docker run -p 8083:8083 -p 8086:8086 --network host --restart always --name influx -v influx_data:/var/lib/influxdb influxdb

docker exec -it influx influx  // Execute container influx and run the command influx (1st containername 2nd operation)

create database mydb
show databases
use mydb
insert table01,value01=100 value02=200
insert table01,value01=10 value02=20
select * from table01
```


```
docker pull ericmick/armhf-mosquitto
docker run -d -p 1883:1883 -p 9001:9001 --network host --restart always --name mybroker  ericmick/armhf-mosquitto:latest
```


You can find several more relevant containers at [Wago's DockerHub Account](https://hub.docker.com/u/wagoautomation) or [here](https://hub.docker.com/search?q=wagoautomation&type=image).


For further software development with regards to Docker, check out their [gitrepo](https://github.com/docker/docker-ce).
