import logging
import os

import webob.dec
import webob.exc

from paste.deploy import loadapp
from wsgiref.simple_server import make_server

import routes.middleware

CONTEXT_ENV='openstack.context'

LOG = logging.getLogger(__name__)

class Controller(object):
    @webob.dec.wsgify
    def __call__(self,req):
    
