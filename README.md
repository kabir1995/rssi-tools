# RSSI Tools
Educational tool to measure fading and shadowing of channels through RSSI

## What is this?
This is a tool for measuring the Received Signal Strength Indication(RSSI) of RF breakout board. To vizualize fading and shadowing effects of the channel between the transmitter and receiver.

## How to use

Install the dependecies.
`sudo apt install python-pip3`
`make install`

### Setting up the boards

On the 'boards' folder, ESPap.ino setups the Access Point, and rssi_meas.ino measures RSSI and sends to serial port.
On our tests ESP32 works better as Access Point and ESP8266 as the RSSI measuring tool.

To compile using the arduino IDE, if you do not have the boards appearing as options. Go to 'File', 'Preferences', and at Additional URLs to board manager add these two URLs separated by a comma. Like the following:

http://arduino.esp8266.com/stable/package_esp8266com_index.json, https://dl.espressif.com/dl/package_esp32_index.json

Upload to the board.

#### Driver problems

If ESP COM port is not connecting you might need to download this driver.

For the ESP32

https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers#windows


For the ESP8266

https://www.robocore.net/tutoriais/como-instalar-o-driver-do-nodemcu.html

### How to start a experiment
Run `make experiment` and open the rssiTool.ipynb file

Execute the cells 

Output will be at `data/` folder
