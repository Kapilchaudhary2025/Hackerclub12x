#!/bin/bash
echo "Installing dependencies for Hacker Club by Kapil..."
sudo apt update
sudo apt install -y python3 python3-pip
pip3 install scapy
echo "Installation complete. Run the tool with: python3 hacker_club.py"