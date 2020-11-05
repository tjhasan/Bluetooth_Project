# MAC Address Tracking Implementation

This repo holds test code which aims to implement the Address-Tracking algorithm described within the research paper "Tracking Anonymized Bluetooth Devices"

The project currently has the following scripts:

Note the the scripts assume that the json packets are properly formatted and filtered.

## Apple Tracking
This script will attempt to follow MAC Addresses from MacOS and iOS BTLE devices. 

## Bose Tracking
This script will attempt to follow MAC Addresses from Sgl Italia Srl, which is used by BOSE products

## Microsoft Tracking
This script will attempt to follow MAC Addresses from Windows 10 devices

## JSON Tester
This script will make sure that the given JSON file does not throw errors in any of the tracking scripts.  
