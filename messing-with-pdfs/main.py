import re
from PyPDF2 import PdfReader, PdfWriter


def data_merge(content):
    lines = content.splitlines()

    for line in lines:
        print(line)


reader = PdfReader("test.pdf")
page = reader.getPage(0)
text = page.extract_text()

start = "<<"
end = ">>"
result = text[text.find(start) + len(start) : text.find(end)]
print(result)
