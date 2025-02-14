import json
from pptx import Presentation 

def ppt_maker(content, file_name):
    # create actual powerpoint object
    ppt = Presentation()

    #Iterate through each section
    for section in content["sections"]:
        content_title = section["title"]
        text_content = section["content"]
        content_type = section["type"]

        if content_type == "raw text":
            #have text slide
            slide = ppt.slides.add_slide(ppt.slide_layouts[1])
            slide_title = slide.shape.title
            slide_text = slide.shapes.placeholders[1]

            slide_title.text = content_title
            slide_text.text = text_content

    # save powerpoint
    ppt.save(file_name)

with open('ppt_test1.txt', 'r') as file:
    txt_contents = file.read()

#turn it into dictionary
json_contents = json.loads(txt_contents)

file_name = json_contents["document_filename"]
content = json_contents

#call pdf_maker method
file = ppt_maker(content, file_name)

