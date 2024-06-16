import unittest
import os
from head_file import *
class TestHead(unittest.TestCase):
    def setUp(self):
        self.textfile = 'test.txt'
        with open(self.textfile, 'w') as file:
            file.write('Huyambus')

    def tearDown(self):
        if os.path.exists(self.textfile):
            os.remove(self.textfile)



