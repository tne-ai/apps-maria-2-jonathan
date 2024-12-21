import json
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle, PageBreak
from reportlab.platypus import PageTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
import matplotlib.pyplot as plt
# from tne.TNE import TNE
#issue is  |\n|

def pdf_maker(content, file_name):
    #create pdf object, set bounds
    pdf = SimpleDocTemplate(file_name, pagesize=letter)

#take in file 
#LOCALLY TEST
with open('test.txt', 'r') as file:
    txt_contents = file.read()

#turn it into dictionary
json_contents = json.loads(txt_contents)

file_name = json_contents["document_filename"]
content = json_contents

#call pdf_maker method
file = pdf_maker(content, file_name)