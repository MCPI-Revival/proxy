# Proxy
A Minecraft Pi Proxy that allow to players to connect to remote servers.

## Getting started
### Prerequisites
To use the proxy you need to have `Python >= 3.7.x` pre-installed.

### Installation
Download and install the proxy from from the Packagecloud Debian repository:
```shell
# If you didn't add the repository yet
curl -s https://packagecloud.io/install/repositories/Alvarito050506/mcpi-devs/script.deb.sh | sudo bash

# Now the actual installation
sudo apt-get install mcpi-proxy
```


## Usage
Run the `mcpip` command as:
```
mcpip src_addr [src_port [dst_port]]
```
Where `src_addr` is a valid internet address and `src_port` and `dst_port` are valid internet ports.

## Licensing
All the code of this project is licensed under the [GNU General Public License version 2.0](https://github.com/MCPI-Devs/proxy/blob/master/LICENSE) (GPL-2.0).

All the documentation of this project is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0) license.

![CC BY-SA 4.0](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)
