# Remote Access with VPN
PLC's are not always very portable. Being able to connect remotely to devices, even if they are already installed at a site, is a game changer. We have previously used OpenVPN for this. Tosibox has now released a Docker container that enables you to establish a VPN connection, without any hardware. By using this container, you will be able to connect to a remote PLC, as long as the PLC has an internet connection.

Kurt Braun has an excellent video on this subject [here](https://www.youtube.com/watch?v=nJU4qUuldYo).

As Kurt also mentions in the video, it is also possible to set up a Tosibox on a whole network, so that all devices/nodes on the network is possible to each remotely. This does not require the Docker container, but a physical box from Tosibox, that is set up by the router.
