import unittest     # Import the Python unit testing framework
import maths        # Our code to test
#from factorial import factorial
#from nntplib import first


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        # Arrange
        a = maths.add(1, 2)       
        
        # Act
        
        # Assert
        self.assertEqual(a, 3)

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        # Arrange
        b = maths.fibonacci(5)       
        
        # Act
        
        # Assert
        self.assertEqual(b, 5)
        
    def test_convert_base_under_10(self):
        ''' Tests the convert_base function for results under 10. '''
        # Arrange
        c = maths.convert_base(100, 49)       
        
        # Act
        
        
        # Assert
        self.assertEqual(c, '2')
        
    def test_convert_base_over_10(self):
        ''' Tests the convert_base function for results over 10. '''
        # Arrange
        d = maths.convert_base(100, 89)       
        
        # Act
        
        
        # Assert
        self.assertEqual(d, 'B')

    def test_add_convert(self):
        ''' Tests the convert_base of the add function. '''
        # Arrange
        a = maths.add(1, 2, 1)      
        
        # Act
        b = maths.convert_base(3, 1)
        
        # Assert
        self.assertEqual(a, b)

    def test_factorial(self):
        f = maths.factorial(5)
        self.assertEqual(f, 120)
        
# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
