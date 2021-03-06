import os
localDir = os.path.dirname(__file__)
absDir = os.path.join(os.getcwd(), localDir)

import cherrypy

class FileDemo(object):

    def index(self):
        return """
        <html>
            <head>
                <script src="js/toggle.js"></script>
            </head>
            <body>
                <script src="/homes/mhroelfes/NetBeansProjects/primerserviceweb/public_html/js/vendor/jquery.js"></script>
                <a href="#" class="small radius button advanced">Advance options</a>
                <div class="toggleTest">
                    vfagfsd
                    gfsdgf
                    sgfsdgf
                    sdgfsdgfs
                    gfsdg
                </div>

                <h2>Upload a file</h2>
                <form action="upload" class="upload" method="post" enctype="multipart/form-data">
                filename: <input type="file" name="myFile" /><br />
                <input type="submit" />
                </form>

            </body>

        </html>
        """
    index.exposed = True

    def upload(self, myFile):
        out = """<html>
        <body>

            myFile dir: %s
        </body>
        </html>"""

        # Although this just counts the file length, it demonstrates
        # how to read large files in chunks instead of all at once.
        # CherryPy reads the uploaded file into a temporary file;
        # myFile.file.read reads from that.
        size = 0
        while True:
            data = myFile.file.read()

            if not data:
                break
            return out % (data)
#           size += len(data)
#         (size, myFile.filename, myFile.content_type, localDir)
    upload.exposed = True



#tutconf = os.path.join(os.path.dirname(__file__), 'tutorial.conf')

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(FileDemo())
else:
    # This branch is for the test suite; you can ignore it.
    cherrypy.tree.mount(FileDemo())
