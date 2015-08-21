try:
   import ConfigParser as ConfigParser
except:
   import configparser as ConfigParser
import requests
from MqttCom import MqttCom

class LandroidM(object):
    ''''Class to handle the Worx Landroid M'''

    def __init__(self, config_file):
        Config = ConfigParser.ConfigParser()
        Config.read(config_file)
        self.config = {}

        # Check for Landroid section
        if Config.has_section("Landroid"):
            self.config['Landroid_Addr'] =  Config.get("Landroid","Addr")
            self.config['Landroid_User'] =  Config.get("Landroid","User")
            self.config['Landroid_Pin'] =   Config.get("Landroid","Pin")
            mqttc = MqttCom(self.config['Mqtt_Host'], int(self.config['Mqtt_Port']))
        else:
            print("Config file must contain 'Landroid' section, see documentation.")

        # Check for Mqtt section
        if Config.has_section("Mqtt"):
            self.config['Mqtt_Host'] =      Config.get("Mqtt","Host")
            self.config['Mqtt_Port'] =      Config.get("Mqtt","Port")
            self.config['Mqtt_BaseTopic'] = Config.get("Mqtt","BaseTopic")

        # Check for Dweet section
        if Config.has_section("Dweet"):
            self.config['Dweet_Thing'] =    Config.get("Dweet","Thing")

    def get_status(self):
        # Poll Landroid Worx
        try:
            response = requests.get(self.config['Landroid_Addr'],
                                    auth=(self.config['Landroid_User'],
                                    self.config['Landroid_Pin']))
            self.json_data = response.json()
        except requests.RequestException as e:
            print(e)

    def send_mqtt_message(self, sub_topic, value):
        topic = self.config['Mqtt_BaseTopic'] + sub_topic
        self.mqttc.publish(topic, value)

if __name__ == '__main__':
    my_landroid = LandroidM('config_default.ini')
    my_landroid.get_status()