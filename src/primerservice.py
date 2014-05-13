# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="mhroelfes"
__date__ ="$Apr 23, 2014 11:07:32 AM$"
import sys
import cherrypy

class PrimerService():
    def __init__(self):
        try:
            self.checkInputFile("example.fasta")
        except Exception as e:
            print(e)





    def checkInputFile(self, file):
        """
            Author: Marco Roelfes
            Checks if uploaded file is in the right format and only contain one sequences

        """

        file = file.split(".")
        if file[-1] != "fasta" and file[-1] != "fa" and file[-1] != "gb":
            raise Exception("Uploaded file has to be in FASTA or GeneBank format")
        





if __name__ == "__main__":
    PrimerService()