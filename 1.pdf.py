import PyPDF2

with open('dummy.pdf', 'rb') as file:
    # rb denotes read binary
    reader = PyPDF2.PdfFileReader(file) 
    # used to read pdf files
    print(reader.numPages)  # 1, returns number of pages
    page = reader.getPage(0) #.getPage(pagenumber) page number starts form zero which is the first page, this method returns the page object
    page.rotateCounterClockwise(90)
    # rotates the pdf counter clock wise by angle 70 degree.
    writer = PyPDF2.PdfFileWriter() 
    # here we opened the writer object    to write object
    writer.addPage(page)    # add the rotated page to the writer object
    with open('rotated.pdf', 'wb') as new_file:
        # we created new file named rotated.pdf to save our changes 
        writer.write(new_file)
     