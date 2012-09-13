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
import tempfile
import json

class Test(unittest.TestCase):
    '''
    classdocs
    '''
    def testGetSinBD(self):
        request = webapp2.Request.blank("/")
        response = request.get_response(service.app)
        self.assertDictEqual(response.body,"")
    
    def testGetConBD(self):
        request = webapp2.Request.blank("/")
        response = request.get_response(service.app)
        data = json.load(open("datos.json", "r"))
        body = json.dumps(data)
        self.assertDictEqual(response.body,body)
        
    
    def testPostJsonSinBD(self):
        request = webapp2.Request.blank("/")
        request.method = 'POST'
        request.body = '{"prueba" : "PostJsonSinBD"}'
        request.headers['Content-Type'] = 'application/json'
        response = request.get_response(service.app)
        data = '{"mensajes" : []}'
        body = json.dumps(data)
        self.assertDictEqual(response.body,body)
        
    
    def testPostTextoSinBD(self):
        request = webapp2.Request.blank("/")
        request.method = 'POST'
        request.body = 'TextoPlano'
        response = request.get_response(service.app)
        data = '{"mensajes" : []}'
        body = json.dumps(data)
        self.assertDictEqual(response.body,body)
    
    def testPostJsonConBD(self):
        data = '{"mensajes" : []}'
        json.dumps(data)
    
    def testPostTextoConBD(self):
        pass
    
    def setUp(self):
        self.old_dir = os.path.abspath(os.curdir) # save old directory
        self.cwd = tempfile.mkdtemp() # new current working directory
        os.chdir(self.cwd)

    def tearDown(self):
        os.chdir(self.old_dir) # restore working directory
        shutil.rmtree(self.cwd) # delete temp directory
    
        