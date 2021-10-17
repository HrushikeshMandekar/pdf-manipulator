# Adding/Merging water marks to the pdf
import PyPDF2

template = PyPDF2.PdfFileReader(open("super.pdf", "rb")) # used shortcut trick to open the file, here we have opened the file on which watermark has to apply

watermark = PyPDF2.PdfFileReader(open("wtr.pdf", "rb")) # opened the file in which watermark is present, which we are going to apply to other files.

writer = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    #.mergePage() will merge the two pages into each other.
    # watermark.getPage(0) here as watermark file have only one page therefore we have written zero index for the first page
    writer.addPage(page) # the merge page is added to the writer object.
    
    with open("watermark.pdf", "wb") as file:
        writer.write(file)