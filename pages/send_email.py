import smtplib, ssl


host = "smtp.gmail.com"
port = 465

username = "emherrer1@gmail.com"
password = "wznwyaghaohfqlfg"

receiver = "emherrer1@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hola
Hola como estas?
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
