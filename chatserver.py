import os

from twisted.application import service, internet
from twisted.internet import reactor

from twisted.web import wsgi
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.web.websockets import WebSocketsResource, lookupProtocolForFactory

from twisted_chat.factories import ChatFactory
from twisted_chat.resources import HttpChat, StaticFileScanner
from twisted_chat.wsgi import WsgiRoot
from twisted.python.threadpool import ThreadPool

from django.core.handlers.wsgi import WSGIHandler



shared_messages = {}

resource = HttpChat(shared_messages)
factory = Site(resource)
ws_resource = WebSocketsResource(lookupProtocolForFactory(resource.wsFactory))

root = Resource()
root.putChild("",resource) 
root.putChild("ws",ws_resource)

application = service.Application("chatserver")
internet.TCPServer(1025, Site(root)).setServiceParent(application)


wsgiThreadPool = ThreadPool()
wsgiThreadPool.start()

django_application = WSGIHandler()
django_resource = wsgi.WSGIResource(reactor, wsgiThreadPool, django_application)

django_root = WsgiRoot(django_resource)
project_dir = os.getcwd()
django_root.putChild('static', StaticFileScanner(project_dir + "/chat/static", project_dir + "/django_twisted_chat/static"))

internet.TCPServer(8001, Site(django_root)).setServiceParent(application)
