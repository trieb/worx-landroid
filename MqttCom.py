import paho.mqtt.client as mqtt

class MqttCom(object):
    '''Class to handle communication over mqtt'''

    def __init__(self, host, port, debug=False):
        self.debug=debug
        # Initiate mqtt-client
        self.mqttc = mqtt.Client()
        self.mqttc.on_connect = self.__on_connect
        self.mqttc.on_message = self.__on_message
        self.mqttc.connect(host, port, 30)
        self.mqttc.loop_start()

    def __on_connect(self, client, userdata, rc):
       if(self.debug):
          print("Connected with result code" + str(rc))

    def __on_message(self, client, userdata, msg):
       if(self.debug):
          print("Received new message ")
          print(msg.topic + ":  " + str(msg.payload))
       #pass

    def publish(self, topic, value):
        self.mqttc.publish(topic, value)

    def loop_stop(self):
        if(self.debug):
            print("Closing connection to mqtt broker.")
        self.mqttc.loop_stop()

