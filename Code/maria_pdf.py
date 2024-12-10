import json
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.platypus import PageTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
import matplotlib.pyplot as plt
#from tne.TNE import TNE

styles = getSampleStyleSheet()
spacer_blank = Spacer(1, 12)
spacer_enter = Spacer(1, 6)

#take in json file contents
#https://www.geeksforgeeks.org/json-load-in-python/
#https://docs.reportlab.com/reportlab/userguide/ch6_paragraphs/

# Initialize the TNE object
#session = TNE(uid=UID, bucket_name=BUCKET, project=PROJECT, version=VERSION)

def pdf_maker(content, file_name):
    #create pdf object, set bounds and spacer
    pdf = SimpleDocTemplate(file_name, pagesize=letter)
    styleN = styles['Normal']
    story = []

    #iterate through each section 
    for section in content["sections"]:
        content_type = section["type"]
        actual_content = section["content"]
    
        if content_type == "raw text":
            #have text/paragraph added to pdf (story object)
            story.append(Paragraph(actual_content, styleN))
            story.append(spacer_blank)
        
        elif content_type == "table":
            #have table added into pdf
            lines = actual_content.strip().split("\n")
            headers = lines[0].split("|") # Extract headers
            rows = [line.split("|") for line in lines[1:]]  # Extract row
            
            table_content = [headers] + rows

            styleT = TableStyle([
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('BOX', (0, 0), (-1, -1), 1, colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTNAME', (0, 1), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10)
            ])
            
            story.append(Table(table_content, style= styleT))
        
        elif content_type == "chart":
            #add chart into pdf

            #load in json formatted content into code
            chart_contents = json.loads(actual_content)

            #depending on type of chart listed
            if(chart_contents['type'] == 'line'):
                print("LINE CHART")

                #get the chart data
                chart_datasets = chart_contents['data']

                #get chart title
                chart_title_display = chart_contents['options']['title']['display']
                chart_title_text = chart_contents['options']['title']['text']

                if(chart_title_display):
                    plt.title(chart_title_text)

                #get chart legend
                chart_legend = chart_contents['options']['legend']['display']

                #BUILD GRAPH HERE
                # get x lables
                x_axis = chart_datasets['labels']

                # get dataset label
                dataset_label = chart_datasets['datasets'][0]['label']

                #get dataset
                dataset = chart_datasets['datasets'][0]['data']

                #build the graph
                plt.plot(x_axis, dataset)
                plt.ylabel(dataset_label)

                if(chart_legend):
                    plt.legend()

                plt.show()

                #get lables
                #print(chart_data)
            else:
                print("SOMETHING ELSE")

            #print(chart_contents)
            continue
    
    #upload pdf to session
    pdf.build(story)

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
