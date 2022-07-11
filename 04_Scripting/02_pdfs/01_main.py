import PyPDF2

#reading a pdf file
#rb stands for read binary
with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    # get the number of pages
    print(reader.numPages)
    # get the page
    print(reader.getPage(0))
    # rotate the page
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    #save the rotated pdf
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as written_file:
        writer.write(written_file)