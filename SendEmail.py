"""La librería smtplib de Python es una herramienta que permite enviar correos electrónicos desde 
un programa Python utilizando el protocolo Simple Mail Transfer Protocol (SMTP)"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

your_email = ""
your_password = ""

recipent = ""

message = MIMEMultipart()
message["From"] = your_email
message["To"] = recipent
message["Subject"] = "Email de ejemplo"

body = "Este es un email enviado como prueba."

message.attach(MIMEText(body, "plain"))

smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.starttls()
smtp_server.login(your_email, your_password)

smtp_server.sendmail(your_email, recipent, message.as_string())
smtp_server.quit()
print("Email enviado.")
