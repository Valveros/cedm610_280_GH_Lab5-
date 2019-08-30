import unittest
from logger import Logger

class target:

    def __init__(self):
        self.__x = None

    def get(self):
        return self.__x

    def set(self, x):
        self.__x = x

class loggerTest(unittest.TestCase):

    def test_info(self):
        ''' Tests the info function. '''
        # Arrange   
        t = target()
        log = Logger()
        a = str(log.info(t.set("msg")))  
        # Act
        b = "msg"
        
        # Assert
        self.assertEqual(t.get(self), b)
        
    def test_error(self, target=None):
        ''' Tests the error function. '''
        log = Logger()
        b = log.error("msg")
        self.assertEqual(b, "msg")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()