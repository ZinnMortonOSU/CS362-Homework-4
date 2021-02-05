import unittest
import cubevolume

class TestCaseCubeVolume(unittest.TestCase):
    def test_Cubevolume(self):
        #Normal test
        self.assertEqual(cubevolume.cubeVolume(5), 125)

        #Float test
        self.assertEqual(cubevolume.cubeVolume(2.5), 15.625)

        #Testing negative input
        try:
            cubevolume.cubeVolume(-5)
        except:
            pass
        else:
            self.fail("Calculator took a negative input")
        
        #Testing complex number
        try:
            cubevolume.cubeVolume(1j)
        except:
            pass
        else:
            self.fail("Calculator took a complex input")
        
        #Testing invalid data type
        try:
            cubevolume.cubeVolume("string")
        except:
            pass
        else:
            self.fail("Calculator took a string")

if __name__ == '__main__':
    unittest.main(verbosity=2)