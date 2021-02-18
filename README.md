# Proxy
A Proxy That Allows Players To Connect To Remote Servers

## Getting started
### Prerequisites
To use the proxy you need to have `Python >= 3.7.x` pre-installed.

### Installation
#### For debian based systems like the Raspberry Pi OS:
Download and install the proxy from releases:
```shell
wget https://github.com/MCPI-Revival/proxy/releases/download/0.3.3/mcpi-proxy_0.3.3.deb
sudo apt-get install ./mcpi-proxy_0.3.3.deb
sudo rm mcpi-proxy_0.3.3.deb
```

#### For Fedora/RedHat/CentOS based OSes
```shell
wget https://github.com/MCPI-Revival/proxy/releases/download/0.3.3/mcpi-proxy_0.3.3.deb
yum -y install  alien   
alien -r mcpi-proxy_0.3.3.deb generated   
rpm -ivh --nodeps --force mcpi-proxy-0.3.3.noarch.rpm  
```
## Usage
Run the `mcpip` command as:
```
mcpip server_addr server_port scr_port
```
Replace server_addr with the server IP. If the server uses a port different from the default one (19132), replace server_port with the different server port. If you want to use a specific port on your device to connect to the server (eg. you have another proxy instance running), replace scr_port with the port you want it to originate from.

## API
The proxy exposes the following methods through the `Proxy` class in the `mcpip` Python 3 module:

### `def __init__()`
Initializes the class.

### `set_option(name, value):`
Sets the `name` option to `value`. Avaiable options:
 + `"src_addr"`: The source address.
   `"src_port"`: The source port.
 + `"dst_port"`: The destination port.

### `def get_options()`
Returns the options as a dictionary.

### `def run()`
Runs the proxy.

### `def stop()`
Stops the proxy.

## Licensing
All the code of this project is licensed under the [GNU General Public License version 2.0](https://github.com/MCPI-Devs/proxy/blob/master/LICENSE) (GPL-2.0).

All the documentation of this project is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0) license.

![CC BY-SA 4.0](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)
