import json
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.platypus import PageTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
#from tne.TNE import TNE

styles = getSampleStyleSheet()
_SPACER = Spacer(1, 12)

#take in json file contents
#https://www.geeksforgeeks.org/json-load-in-python/
#https://docs.reportlab.com/reportlab/userguide/ch6_paragraphs/

# Initialize the TNE object
#session = TNE(uid=UID, bucket_name=BUCKET, project=PROJECT, version=VERSION)

def pdf_maker(content, file_name):
    #create pdf object
    pdf = SimpleDocTemplate(file_name, pagesize=letter)
    styleN = styles['Normal']
    story = []

    #set x and y axis
    x = 100
    y = 750

    #iterate through each section 
    for section in content["sections"]:
        content_type = section["type"]
        actual_content = section["content"]
    
        if content_type == "raw text":
            #have text/paragraph added to pdf
            story.append(Paragraph(actual_content, styleN))
            story.append(_SPACER)
        
        elif content_type == "table":
            #have table added into pdf
            continue
        
        elif content_type == "chart":
            #add chart into pdf
            continue
    
    #upload pdf to session
    pdf.build(story)
    #pdf.save()
    #session.upload_object(file_name, pdf)


#take in file 
with open('test.txt', 'r') as file:
    txt_contents = file.read()

#turn it into dictionary
json_contents = json.loads(txt_contents)

file_name = json_contents["document_filename"]
content = json_contents

#call pdf_maker method
file = pdf_maker(content, file_name)

#print(json_contents)