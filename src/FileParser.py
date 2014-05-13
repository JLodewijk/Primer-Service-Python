# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Jeroen Lodewijk <j.lodewijk@st.hanze.nl>"
__date__ ="$Apr 23, 2014 11:22:41 AM$"
from Bio import GenBank
from Bio import SeqIO
"""
Author: Jeroen Lodewijk <j.lodewijk@st.hanze.nl> and Marco Roelfes <marcoroelfes@gmail.com>
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
    def readFastaFile(file):
        """Help on function ReadFastaFile:

            ReadFastaFile(file)

	Return a list contains sequences of a that particular file."""
        sequences = {}
        sequenceOfLine = ""
        for line in open(file):
            line = line.strip()
            if line.startswith(">"):
                title = line
            if ">" not in line:
                # Add all the sequences to one string of one fasta entry.
                sequenceOfLine = sequenceOfLine + line
            else:
                #Prevent empty sequenceOfLine of appending into self.sequence
                if sequenceOfLine != "":
                    sequences[title]= sequenceOfLine
                    sequenceOfLine = ""
        #To append the last sequence in the file as well.
        sequences[title]= sequenceOfLine
        return sequences


    def readGeneBankFile(file):
        """
            Author: Marco Roelfes
            readGeneBankFile(file)
            file: genebank file
            readGeneBankFile reads genebank files to a dictionary(key: title(definition+accession+locus+source), value: sequence)
            returns dictionary with key: title and value: sequence
        """
        sequences = {}
        #loop trough record to parse sequence in Seq object
        for gb_record in SeqIO.parse(open(file,"r"), "genbank") :
            #set seq
            seq = gb_record.seq



        #loop through file to parse headers
        for record in GenBank.parse(open(file)):
            #set title
            title=">" + record.definition + "accesion: " + record.accession[0] + " " +record.locus +" " + record.source
        #put title,sequence to dictionary sequences
        sequences[title] = seq
        return sequences

if __name__ == "__main__":
    FileParser()
