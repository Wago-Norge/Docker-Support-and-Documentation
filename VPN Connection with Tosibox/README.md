# Remote Access with VPN
PLC's are not always very mobile. Being able to connect remotely to devices, even if they are already installed at a site, is a game changer. We have previously used OpenVPN for this. Tosibox has now released a Docker container that enables you to establish a VPN connection, without any hardware. By using this container, you will be able to connect to a remote PLC, as long as the PLC has an internet connection.

Link to DockerHub: https://hub.docker.com/r/wagoautomation/softx-openwrt

Kurt Braun has an excellent video on this subject [here](https://www.youtube.com/watch?v=nJU4qUuldYo).

As Kurt also mentions in the video, it is also possible to set up a Tosibox on a whole network, so that all devices/nodes on the network is possible to each remotely. This does not require the Docker container, but a physical box from Tosibox, that is set up close to the router.

### Prerequesites
This walkthrough assumes that you have Docker installed according to our [guide](https://github.com/Wago-Norge/Docker-Support-and-Documentation/tree/master/Installing%20Docker), and that you have a working internet connection. You must also have a Tosibox Key, to license the software. Lastly, a Windows computer with Tosibox Key Software is needed.

#### Necessary settings
The following settings may be necessary to apply in Web Based Management:

1. Configure static IP:
Under Networking > TCP/IP, configure a static IP on the ethernet port that has an internet connection. This may require that you configure the router's DHCP settings, to avoid IP conflicts.
2. Routing:
Under Networking > Routing, make sure to enable IP Forwarding through multiple instances. Thereafter, configure a static route below:
Gateway address should be the IP gateway of the network: the IP address of the router. Gateway Metric should be 20. Make sure to enable the route, and submit.

#### Install the Container
1. Connect to the PLC using a SSH terminal: `root@192.168.1.17`. Use the IP address of your PLC. Username is `root` and password is `wago` per default.
2. Pull the image: `docker pull wagoautomation/softx-openwrt`.
3. Run the docker image: `docker run -d --name lock-softx --cap-add=NET_ADMIN --cap-add=SYS_PTRACE --restart always -p 8000:80 -h "LockForContainer" wagoautomation/softx-openwrt:latest`

#### Configure the Tosibox
1. Connect to the container's interface, by entering http://[IP]:8000 in your web browser.
If the status says the Internet Connection is OK, you are good to go. If not, and you recently started the container, wait a few minutes.
2. Go to Settings > Keys and Locks. Generate a matching key at the bottom of the page.
3. While in Tosibox Key Software on Windows, connect the Tosibox USB Key.
If you have a different product from Tosibox, you may have to skip this step.
4. Under Devices > Remote Matching, enter the key that was generated two steps ago.

The container should now show up in the Key Software. You can test the connection by going connecting to the container in the software, go to a different network (etc), and go the IP address of the container (displayed in the Key Software).
