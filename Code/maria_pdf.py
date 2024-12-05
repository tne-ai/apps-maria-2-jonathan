import json
from reportlab.pdfgen import canvas

pdf = canvas.Canvas("test1.pdf")

pdf.setTitle("Document Title")

pdf.drawString(100, 750, "Hello World")

pdf.save()