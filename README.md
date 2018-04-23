# unicornhat-hd-examples
A collection of unicorn hat hd examples ready to use with Isaax.

# Environments

- Raspberry Pi Zero W
- Raspbian Strech Lite
- SD Card 8GB

# Installation

```
sudo raspi-config nonint do_spi 0
sudo reboot
```

```
sudo apt update && sudo apt upgrade
sudo apt install python3-pip python3-dev python3-spidev
sudo apt install libatlas-base-dev
sudo pip3 install unicornhathd numpy
```

