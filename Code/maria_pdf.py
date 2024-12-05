import json
from reportlab.pdfgen import canvas

#take in json file contents
#https://www.geeksforgeeks.org/json-load-in-python/
with open('test.json', 'r') as file:
    json_contents = json.load(file)

pdf = canvas.Canvas("test2.pdf")

title = json_contents.get("title", "Untitled")
body_text = json_contents.get("bodyText", "Empty")
table_data = json_contents.get("tableData", "Empty")
chart_data = json_contents.get("chartData", "Empty")
sub_head = json_contents.get("subhead", "Empty")
details = json_contents.get("details", "Empty")
recommendations = json_contents.get("recommendations", "Empty")
request_and_response = json_contents.get("request_and_response_issues", "Empty")

pdf.drawString(100, 750, title)

pdf.drawString(100, 750, body_text)

pdf.save()