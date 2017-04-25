
import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#Register unit tests from modules here
# from home.tests import HomeTest
from rba.tests import RbaApiTest

if __name__ == '__main__':
    unittest.main()