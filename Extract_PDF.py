# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('PDF_file.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
pgno=pdfReader.numPages
print(pgno)

for i in range(pgno):
  # extracting text from page
  # creating a page object
    pageObj = pdfReader.getPage(i)
    file=pageObj.extractText()
    file=file.replace("\n", "")
    print(file)

# closing the pdf file object
pdfFileObj.close()
