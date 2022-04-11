import imaplib
import email
import smtplib

email_address = ""
password = ""
def set_credentials(email_addresss,passwords):
    email_address = email_addresss
    password = passwords
def check_inbox(FROM = None,TO = None,SUBJECT = None,Date = None,BCc = None,MESSAGE_NUM = None):
    imap_server = "imap.gmail.com"


    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(email_address, password)

    imap.select("Inbox")
    _, msgnums = imap.search(None, "ALL")

    for msgnum in msgnums[0].split():

        _, data = imap.fetch(msgnum, "(RFC822)")

        message = email.message_from_bytes(data[0][1])
        arr1 = [message.get('From'),message.get('To'),message.get('BCC'),message.get('Date'),message.get('Subject')]
        arr2 = [FROM,TO,SUBJECT,Date,BCc,MESSAGE_NUM]
        print = True
        for i in range(0,6):
            if arr2[i] !=None and arr1[i] !=arr2[i]:
                print=False
        if print:
            print(f"Message Number: {msgnum}")
            print(f"From: {message.get('From')}")
            print(f"To:: {message.get('To')}")
            print(f"BCC: {message.get('BCC')}")
            print(f"Date: {message.get('Date')}")
            print(f"Subject: {message.get('Subject')}")

            print("Content")
            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    print(part.as_string())
    imap.close()
def send_email(to,message,cur_email = email_address,cur_password = password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    try:
        server.login(cur_email,cur_password)
    except:
        print("invalid credentials")
    try:
        server.sendmail(cur_email,to,message)
    except:
        print("could not send message")