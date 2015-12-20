'''
Created on Dec 20, 2012

@author: peng
'''
import unittest
import timeutils


class Test(unittest.TestCase):

    def test_timeutils(self):
        print timeutils.utc_timestamp()
        print timeutils.get_last_week()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_timeutils']
    unittest.main()
