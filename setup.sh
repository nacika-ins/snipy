#!/bin/bash

brew install qt
mkdir ~/tmp
cd ~/tmp
git clone https://github.com/PySide/pyside-setup.git 
cd pyside-setup
easy_install -U PySide
pyside_postinstall.py -install

