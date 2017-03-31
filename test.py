from twisted.application.service import Application
from twisted.internet import reactor
import sys

def print_path():
    print "   ----    The path to the twistd python is: " + str(sys.executable) + "   ----"
    reactor.stop()

application = Application("path_test")
reactor.callWhenRunning(print_path)
