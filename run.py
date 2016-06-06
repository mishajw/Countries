#!/usr/bin/python

import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

message = """"""

def main():
    (code, name) = get_country()
    send_email(code, name)

    with open("dynamic/done.txt", 'a') as f:
        f.write("%s|%s\n" % (code, name))

def get_country():
    # Load the lists
    done = read_list("dynamic/done.txt")
    total = read_list("static/all.txt")

    # Get the undone countries
    undone = [c for c in total if c not in done]

    # Pick a random one
    chosen = random.choice(undone)
    chosen_split = chosen.split("|")
    chosen_code = chosen_split[0]
    chosen_name = chosen_split[1]

    return (chosen_code, chosen_name)

def send_email(code, name):
    recipients = [r.strip() for r in read_list("dynamic/recipients.txt")]

    msg = MIMEMultipart()
    msg["Subject"] = "Country Club"
    msg["To"] = ", ".join(recipients)

    body = get_body(code, name)
    msg.attach(body)

    print(msg.as_string())

    smtp = smtplib.SMTP_SSL("smtp.zoho.com", 465)
    (user, password) = get_auth()
    smtp.login(user, password)
    smtp.sendmail("countries@mishawagner.com", recipients, msg.as_string())

def get_body(code, name):
    return MIMEText("""Country Club!

Test email, ignore

The country of the week is: %s
The Wikipedia page is: https://en.wikipedia.org/wiki/%s
The flag can be found at: https://raw.githubusercontent.com/hjnilsson/country-flags/master/png1000px/%s.png

P.S. Flags may not work if it's a US state, and sometimes the Wikipedia link is broken, soz
    """ % (name, name.replace(" ", "_"), code.lower()))

def get_auth():
    with open("dynamic/login.txt", 'r') as f:
        lines = f.readlines()
        return (lines[0].strip(), lines[1].strip())

def read_list(path):
    with open(path, 'r') as f:
        return [l.strip() for l in f.readlines()]
    
if __name__ == "__main__":
    main()

