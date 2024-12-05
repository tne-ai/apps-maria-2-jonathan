import json
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

#take in json file contents
#https://www.geeksforgeeks.org/json-load-in-python/
#https://docs.reportlab.com/reportlab/userguide/ch6_paragraphs/

#take in file 
with open('test.txt', 'r') as file:
    txt_contents = file.read()

#turn it into dictionary
json_contents = json.loads(txt_contents)

print(json_contents)