##### Development of this repository has been stopped in favour of https://github.com/getavalon/docker

# Goal

To provide simple entry points into Avalon.

# Usage

Download the [zip](https://github.com/tokejepsen/avalon-environment/archive/master.zip), extract and use any of the entry points provided. Initial setup will take a while depending on your internet connection.

# Entry points

All entry points will ensure that all dependencies of Avalon is installed.

## Server

This will launch the MongoDB server.

This takes an optional argument to specify a custom database location. For example ```server C:\data\custom```. If no argument is specified the default location will be used ```C:\data\db```.

## Launcher

This will launch the Avalon launcher. Make sure the server is running before.

## Terminal

This will launch a terminal with all Avalon dependencies available.

# About

When using any of the entry points, the dependencies of Avalon will be installed. The dependencies include:

- mongodb 3.4.10
- python 3.6.5
- git 2.14.1
- pymongo 3.6.1
- pyqt5 5.7.1

The installation is powered by [Miniconda](https://conda.io/miniconda.html), which gets installed to ```[avalon-environment]/bin/miniconda```. The Conda environment is located at ```[avalon-environment]/bin/miniconda/envs/avalon-environment```.

Once all dependencies are downloaded and installed, this repository will get expanded to around 1.6 GB on disk.

## Uninstall

You can find an uninstaller at ```[avalon-environment]/bin/miniconda/Uninstall-Miniconda2.exe```.

Alternatively you can also just delete ```[avalon-environment]/bin/miniconda```, as this directory contains all files from the installation.
