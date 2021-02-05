import unittest
import namegenerator

class TestNameGenerator(unittest.TestCase):
    def test_NameGenerator(self):
        #Normal test
        self.assertEqual(namegenerator.nameGenerator("Zinn","Morton"), "Zinn Morton")
        self.assertEqual(namegenerator.nameGenerator("Joe","Mama"), "Joe Mama")

        #Invalid first name
        try:
            namegenerator.nameGenerator(1,"Test")
        except:
            pass
        else:
            self.fail("nameGenerator took invalid first name") 

        #Invalid last name
        try:
            namegenerator.nameGenerator("test",2.5)
        except:
            pass
        else:
            self.fail("nameGenerator took invalid last name") 

        #Empty first name
        try:
            namegenerator.nameGenerator("","test")
        except:
            pass
        else:
            self.fail("nameGenerator took empty first name")

        #Empty last name
        try:
            namegenerator.nameGenerator("test","")
        except:
            pass
        else:
            self.fail("nameGenerator took empty last name")
        

if __name__ == '__main__':
    unittest.main(verbosity=2)