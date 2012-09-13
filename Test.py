'''
Created on 13-09-2012

@author: SLP
'''
import sys
# para Python 2.6 o inferior, utilizamos unittest2
if sys.hexversion < 0x2070000:
    import unittest2 as unittest
else:
    import unittest
import Main
import os
import shutil

class Test(unittest.TestCase):
    '''
    classdocs
    '''
    def testGetSinBD(self):
        request = webapp2.Request.blank("/")
        response = request.get_response(service.app)
        response2 = webapp2.Response.body('status 404')
        self.assertDictEqual(response, response2)
        pass
    
    def testGetConBD(self):
        pass
    
    def testPostJsonSinBD(self):
        pass
    
    def testPostTextoSinBD(self):
        pass
    
    def testPostJsonConBD(self):
        pass
    
    def testPostTextoConBD(self):
        pass
    
    def setUp(self):
        self.old_dir = os.path.abspath(os.curdir) # save old directory
        self.cwd = tempfile.mkdtemp() # new current working directory
        os.chdir(self.cwd)

    def tearDown(self):
        os.chdir(self.old_dir) # restore working directory
        shutil.rmtree(self.cwd) # delete temp directory
    
        