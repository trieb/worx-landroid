#!/usr/bin/python
# -*- coding: utf-8 -*-

import ConfigParser
import time
import paho.mqtt.client as mqtt
import dweepy
import requests

DEBUG = True

Config = ConfigParser.ConfigParser()
Config.read('config.conf')

def on_connect(client, userdata, rc):
   if(DEBUG):
      print "Connected with result code", str(rc)
   # Subscribe on connect to reconnect if connection is lost
   
def on_message(client, userdata, msg):
   if(DEBUG):
      print "Received new message "
      print msg.topic, ": ", str(msg.payload)
   pass

# Initiate mqtt-client
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect(Config.get("Mqtt", "Host"), Config.get("Mqtt", "Port"), 60)
mqttc.loop_start()

running = True

while running:
   # Poll Landroid Worx
   response = requests.get(Config.get("Landroid", "Addr"), auth=(Config.get("Landroid", "User"),Config.get("Landroid", "Pin")))
   data = response.json()
   
   battery = "%.1f" % float(data['perc_batt'])
   if(DEBUG):
      print "Battery: ", battery
   topic = Config.get("Mqtt", "BaseTopic") + "battery/"
   #mqttc.publish("laxryggen/landroid/battery", battery);
   mqttc.publish(topic, battery);
 
   # Dweet.io the average ourdoor temperature
   try:
      if(DEBUG):
         print "Landroid-Worx data: ", battery
      dweepy.dweet_for(Config.get("Dweet", "Thing"), {'battery': str(battery)})
   except:
      if(DEBUG):
         print "Dweet error!"
      pass
 
   # Wait, and then exit program  
   time.sleep(5)
   mqttc.loop_stop()
   running = False
   
