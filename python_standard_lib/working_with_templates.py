from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())


message = MIMEMultipart()
message["from"] = "TestAutomation"
message["to"] = "testauto@gmail.com"
message["subject"] = "This is a test"
body = template.substitute({"name": "John"})
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("test.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("testauto@gmail.com", "Automation123")
    smtp.send_message(message)
    print("Sent...")
