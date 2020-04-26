import PyPDF2
import sys

input_file = sys.argv[1]
marker_file = sys.argv[2]

template = PyPDF2.PdfFileReader(open(input_file, 'rb'))
watermark = PyPDF2.PdfFileReader(open(marker_file, 'rb'))
output = PyPDF2.PdfFileWriter()

for j in range(template.getNumPages()):
	page = template.getPage(j)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)
	
with open('watermarked.pdf', 'wb') as new_file:
	output.write(new_file)
