# encoding: utf-8

import unittest
from os.path import dirname, abspath, join
from base64 import decodestring, b64encode
from subprocess import call
from time import sleep
from restfulie import Restfulie
from should_dsl import *

FOLDER_PATH = abspath(dirname(__file__))
class MetadataServiceTest(unittest.TestCase):

    def test_extraction(self):
        pdf = open(join(FOLDER_PATH, 'teste.pdf')).read()
        pdf64 = b64encode(pdf)
        pdf64 = "dasdasih"
        service = Restfulie.at("http://localhost:8887/").auth('test', 'test').as_('application/json')
        response = service.post(doc=pdf64, filename='test.pdf')
        resource = response.resource()
        resource.doc_key |should_not| equal_to(None)
        sleep(5)
        response = service.get(key=resource.doc_key).resource()
        response.done |should| equal_to(True)
    
    def test_extraction_with_parameter_metadata(self):
        pdf = open(join(FOLDER_PATH, 'teste.pdf')).read()
        pdf64 = b64encode(pdf)
        pdf64 = "dasdasih"
        service = Restfulie.at("http://localhost:8887/").auth('test', 'test').as_('application/json')
        response = service.post(doc=pdf64, filename='test.pdf')
        resource = response.resource()
        resource.doc_key |should_not| equal_to(None)
        sleep(5)
        
        response = service.get(key=resource.doc_key, metadata=True).resource()
        metadata_key = response.metadata_key
        metadata_key |should_not| equal_to(None)

        sam = Restfulie.at('http://0.0.0.0:8888/').auth('test', 'test').as_('application/json')
        resource = sam.get(key=metadata_key).resource()
        resource.data.autor |should| equal_to('Jose')

if __name__ == '__main__':
    metadataservice_ctl = join(FOLDER_PATH, '..', 'bin', 'metadataservice_ctl')
    try:
        call("%s start" % metadataservice_ctl, shell=True)
        sleep(5)
        unittest.main()
    finally:
        call("%s stop" % metadataservice_ctl, shell=True)