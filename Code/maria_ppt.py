import json
from io import BytesIO
from pptx import Presentation

def ppt_maker(content, file_name):
    #create ppt object, 
    ppt = Presentation()

#turn file into dictionary
json_contents = json.loads(PROCESS_INPUT)

file_name = json_contents["document_filename"]
content = json_contents

#call ppt_maker method
result = ppt_maker(content, file_name)