# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="mhroelfes"
__date__ ="$May 13, 2014 2:59:23 PM$"

import cherrypy


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        host = cherrypy.request.headers['Host']
        return "You have successfully reached " + host

cherrypy.quickstart(HelloWorld())
