# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="mhroelfes"
__date__ ="$Apr 23, 2014 11:07:32 AM$"
import sys
import cherrypy

class HelloWorld(object):
    def index(self):
        return "Hello World!"
    index.exposed = True

cherrypy.quickstart(HelloWorld())

#class PrimerService():
#    def __init__(self):
#        print("main program")
#        print(sys.path)
#
#if __name__ == "__main__":
#    PrimerService()