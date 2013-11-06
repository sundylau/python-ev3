from __future__ import print_function
import unittest

from ev3 import robot
from test import test_util

def setUpModule():
    robot.open_all_devices()
    
def tearDownModule():
    robot.close_all_devices()
class TestEv3Sensors(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
        

    def setUp(self):
        print ("In method", self._testMethodName)
        
    def test_mindsensor_psp_sensor(self):
        from ev3.mindsensor import PSP

        pspSensor = PSP(robot.SENSOR_1)
        print("press up")
        test_util.count_down(3)
        test_util.wait(5, lambda:print(pspSensor.get_up()))
        print("press down")
        test_util.count_down(3)
        test_util.wait(5, lambda:print(pspSensor.get_down()))
        print("left stick")
        test_util.count_down(3)
        test_util.wait(5, lambda:print(pspSensor.get_x_left()))
    @classmethod
    def tearDownClass(cls):
        pass
        


if __name__ == '__main__':
    unittest.main()