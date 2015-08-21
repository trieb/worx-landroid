import json
import unittest
try:
   import ConfigParser as ConfigParser
except:
   import configparser as ConfigParser
from LandroidM import LandroidM

class TestLandroidMClass(unittest.TestCase):

    def setUp(self):
        config_file = 'test_data/config_test.ini'
        self.Config = ConfigParser.ConfigParser()
        self.Config.read(config_file)
        self.my_landroid = LandroidM(config_file)

    def test_init_class_from_config_file(self):
        '''Init class with config file and check parameters'''

        self.assertEqual(self.my_landroid.config['Mqtt_Host'],      self.Config.get("Mqtt","Host"))
        self.assertEqual(self.my_landroid.config['Mqtt_Port'],      self.Config.get("Mqtt","Port"))
        self.assertEqual(self.my_landroid.config['Mqtt_BaseTopic'], self.Config.get("Mqtt","BaseTopic"))
        self.assertEqual(self.my_landroid.config['Landroid_Addr'],  self.Config.get("Landroid","Addr"))
        self.assertEqual(self.my_landroid.config['Landroid_User'],  self.Config.get("Landroid","User"))
        self.assertEqual(self.my_landroid.config['Landroid_Pin'],   self.Config.get("Landroid","Pin"))
        self.assertEqual(self.my_landroid.config['Dweet_Thing'],    self.Config.get("Dweet","Thing"))

    def test_get_status(self):
        '''Parse json for alarm status'''

        data_file = 'test_data/test_response.json'
        with open(data_file) as file:
            data = json.load(file)

        self.my_landroid.get_status()




if __name__ == '__main__':
    unittest.main()