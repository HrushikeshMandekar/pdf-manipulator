# combining multiple files
import PyPDF2
import sys

input = sys.argv[1:] # to take all input

def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_merger(input)