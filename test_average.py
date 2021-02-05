import unittest
import average

class TestAverage(unittest.TestCase):
    def test_Average(self):
        #Normal test
        self.assertEqual(average.average([1,2,3]), 2)
        self.assertEqual(average.average([1,2,3,4]), 2.5)

        #Negative numbers and 0
        self.assertEqual(average.average([-1,0,1]), 0)

        #Float test
        self.assertEqual(average.average([1,2,3,4.5]), 2.625)

        #Testing list of length 1
        self.assertEqual(average.average(5), 5)
        self.assertEqual(average.average(5.2), 5.2)

        #Testing non-list 
        try:
            average.average("test")
        except:
            pass
        else:
            self.fail("Calculator took a string")

        #Testing empty list
        try:
            items = []
            average.average(items)
        except:
            pass
        else:
            self.fail("Calculator took an empty list") 

        #Testing list that contains a non int/float
        try:
            items = [1,2,"test"]
            average.average(items)
        except:
            pass
        else:
            self.fail("Calculator took a list with a non-int/double") 
        

if __name__ == '__main__':
    unittest.main(verbosity=2)