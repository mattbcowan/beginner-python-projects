import re
import PyPDF2 as pdf


def data_merge(content):
    lines = content.splitlines()

    for line in lines:
        print(line)


file = open("test.pdf", "rb")
reader = pdf.PdfReader(file)
page = reader.getPage(0)
text = page.extract_text()

start = "<<"
end = ">>"
text_before = text[: text.find(start)]
# text_to_replace = text[text.find(start) + len(start) : text.find(end)]
replacement_text = " LOL "
text_after = text[text.find(end) + 2 :]

replaced_text = text_before + replacement_text + text_after

text = replaced_text

writer = pdf.PdfWriter()


print(replaced_text)
