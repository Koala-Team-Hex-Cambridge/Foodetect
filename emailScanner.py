import imaplib
import email
from email.header import decode_header
import webbrowser
import os

attachment_dir = 'C:/Users/kmong/OneDrive/Documents/VisualStudioCode/HackCambridge/Foodete'

class FileLocation:
    def __init__ (self, givenEmail, givenProvider, givenPassword):
        imap = auth(givenEmail, givenProvider, givenPassword)
        imap.select("INBOX")

        result, data = imap.fetch(b"10", "(RFC822)")
        raw = email.message_from_bytes(data[0][1])

        msgs = get_emails(search("FROM", "no-reply@mail.tesco.com", imap))

        for msg in msgs:
            print(get_body(email.message_from_bytes(msg[])))

        # close the connection and logout
        imap.close()
        imap.logout()


    def auth(self, givenEmail, givenProvider, givenPassword):
        # linking provider to imap
        addressDictonary = {
            "gmail": 'imap.gmail.com',
            "outlook": 'imap-mail.outlook.com',
            "office365": 'outlook.office365.com',
            "yahoo": 'imap.mail.yahoo.co.uk',
            "verizon": 'incoming.verizon.net',
        }

        imap_url = addressDictonary[str(emailProvider)]
        
        # create an IMAP4 class with SSL
        imap = imaplib.IMAP4_SSL(imap_url)

        email = givenEmail
        password = givenPassword 

        # authenticate
        imap.login(email, password)


    def get_body(self, msg):
        if msg.is_multipart():
            return get_body(msg.get_payload(0))

        else:
            return msg.get_payload(None, True)

    #very important for me to get the information
    def get_attachments(self, msg):
        for part in msg.walk(): #going through the connents of the message
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Dispostion') is None:
                continue 
            fileName = part.get_filename()

            if bool(fileName):
                filePath = os.path.join(attachment_dir, fileName)
                with open(filePath, 'wb') as f:
                        f.write(part.get_payload(decode=True))

    def search(self, key, value, imap):
        results, data = imap.search(None, key, '"{}'.format(value))
        return data

    def get_emails(self, result_btyes):
        megs = []
        for nums in result_btyes[0].split():
            typ, data = imap.fetch(num, "(RFC822)")
            msgs.append(data)
        return msgs
