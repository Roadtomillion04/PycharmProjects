# unittest is the way we test the other file working fine or not
# the test should be more descriptive
import unittest
import main

# first we create class and pass unittest.TestCase
class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_num = 10
        result = main.do_stuff(test_num)
        self.assertEqual(result, 15) # assertEqual take 2 args and checks them equal

    def test_do_stuff2(self):
        test_num = "sdsa"
        result = main.do_stuff(test_num)
                                    #obj  , class
        self.assertTrue(isinstance(result, ValueError)) # make sure do_stuff() returns valueError

    def to_do_stuff3(self):
        test_num = None
        result = main.do_stuff(test_num)

        self.assertEqual(result, "Invalid")

    def to_do_stuff4(self):
        test_num = ''
        result = main.do_stuff(test_num)

        self.assertEqual(result, "Invalid")


#to run it
if __name__ == '__main__':
    unittest.main()

