# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Jeroen Lodewijk <j.lodewijk@st.hanze.nl>"
__date__ ="$Apr 23, 2014 11:22:41 AM$"

"""
Author: Jeroen Lodewijk <j.lodewijk@st.hanze.nl>
Script name: fileparser

Fileparser is capable of parsing fasta and genebank files. 
These two file types are handled both in different functions, the fasta file is handled in the ReadFastaFile. 
The genebank file in the ReadGeneBankFile.

Purpose of FileParser:
    Reading of fasta files, taking the sequence segment of every entry. 
    Reading of genebank files, taking the coding regions out of the genebank file.

The input of FileParser is:
    file:
        Either a genebank or fasta file containing genetic information.

The output of FileParser is:
        self.sequence:
            List containing all the sequences within that particular file.

"""

class FileParser():
    """FileParser() -> FileParser
	
	Create a new FileParser object."""
    def __init__(self):
        """Help on function __init__: 
		
            __init__(self)
		
	Create a new FileParser object."""
        self.sequences = []
        self.ReadFastaFile("example.fasta")
        
    def ReadFastaFile(self, file):
        """Help on function ReadFastaFile: 
		
            ReadFastaFile(self, file)
		
	Return a list contains sequences of a that particular file."""
        sequenceOfLine = ""
        for line in open(file):
            line = line.strip()
            if ">" not in line:
                # Add all the sequences to one string of one fasta entry.
                sequenceOfLine = sequenceOfLine + line
            else:
                #Prevent empty sequenceOfLine of appending into self.sequence
                if sequenceOfLine != "":
                    self.sequences.append(sequenceOfLine)
                    sequenceOfLine = ""
        #To append the last sequence in the file as well.
        self.sequences.append(sequenceOfLine)
        return self.sequences
    
    def ReadGeneBankFile(self, file):
        pass

if __name__ == "__main__":
    FileParser()
