import unittest
try:
   import ConfigParser as ConfigParser
except:
   import configparser as ConfigParser
from MqttCom import MqttCom


class TestMqttComClass(unittest.TestCase):

    def setUp(self):
        self.mqttc = MqttCom('trieb.asuscomm.com', 1883, True)

    def test_publish(self):
        '''Publish message'''
        self.mqttc.publish("testing/from/office", "tjo")

    def tearDown(self):
        self.mqttc.loop_stop()


if __name__ == '__main__':
    unittest.main()
