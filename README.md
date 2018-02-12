# Luggauge

An essential traveller needs to make sure that his luggauge is handled properly on his flight when he goes on vacation. To supplement this our team at Imperial College London created a smart IoT sensor that is able to use acceleration values from an accelerometer coupled with the added use of an LDR to broadcast impact values (above a certain threshold) and times when the suitcase was opened (light was shined on the LDR). 

This repository includes all of the software required for the development of the IoT sensor. It assumes that any user has the following material:

- An LIS3DH 3 axis (by default) Accelerometer. <----[click me](http://www.st.com/content/ccc/resource/technical/document/datasheet/3c/ae/50/85/d6/b1/46/fe/CD00274221.pdf/files/CD00274221.pdf/jcr:content/translations/en.CD00274221.pdf)

- An ESP8266 on a Node MCU. <-----[click me](http://www.nodemcu.com/index_en.html)

- A light dependent resistor.

- x6 Jumper Cables. 

- A USB to serial connection for the Node MCU to a laptop (included with the Node MCU on purchase). 

- A 4k7 ohms resistor, used as a potential divider for the LDR. 

- An LED (To indicate statuses of time retrieval from a broker and pushing of data to the web).

## Usage

To utilise any elements of this repository you must have some familiarity with Git and Terminal. 

Begin with a git clone of the repository by:

`$ git clone https://github.com/Afrazinator/Luggauge.git`

Then navigate into the repository with:

`$ cd Luggauge`

If you type:

`$ ls`

You will see all of the files:

- main.py (the brains behind the code, which does everything. Reads the values and sends them to an MQTT Broker)
- formattime.py (Displays the date and time as hh:mm:ss dd/mm/yy)
- manipulatingdata.py (Performs a standardisation of the acceleration values and returns them in m/s^2)

All of these files need to be present on the NodeMCU. In fact the NodeMCU has a nifty feature which allows it to execute the 'main.py' file on startup. So after adding these files to the NodeMCU using a serial connection, the NodeMCU interfaced with the Accelerometer and an LDR should send the acceleration values to an MQTT Broker. 

A good review of the board setup is available in this repository under 2 JPEG files that illustrate the correct connections that must be made. 

To change the MQTT Broker you must examine the relevant line in 'main.py' which includes the method `sta_if.connect('EEERover','exhibition')` where the relevant params are `sta_if.connect('NAME','PASSWORD')` 

## Dependencies 

None are required as upython once installed on the NodeMCU should include all of the relevant and required libraries. 
