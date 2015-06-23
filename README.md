# worx-landroid

This script polls the Landroid-Worx for data over REST-api and publish it to a Mqtt-brooker using the Paho Mqtt Client.
It also publish the data using Dweet.io to easily view it on e.g. freeboard.io.  

# To get started

1. Copy config_default.ini to config.ini 
2. Add your configuration to config.ini
3. Install required libraries


# Alarms

The alarms below are being pushed if alarm is given. 
A general alarm_ok = 1 if any of the alarms below are high.  

"allarmi": [ // Alarms
0, blade_blocked
1, repositioning_error 
2, outside_wire
3, blade_blocked
4, outside_wire
5, mower_tilted
6, error 
7, error
8, error
9, collision_sensor_blocked
10,  
11, charge_error
12, battery_error
13, 
14,
15,
16,
17,
18,
19,
20,
21,
22,
23,
24,
25,
26,
27,
28,
29,
30
],