import json
from reportlab.pdfgen import canvas

pdf = canvas.Canvas("test1.pdf")

pdf.setTitle("Document Title")

pdf.save()