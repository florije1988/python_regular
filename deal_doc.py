# -*- coding: utf-8 -*-
__author__ = 'florije'
from docx import Document

document = Document('test.docx')
author = document.core_properties.author
print(author)
for paragraph in document.paragraphs:
    print(paragraph.text)
