import imaplib
import email
from email.header import decode_header
import webbrowser
import os


def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)


def emailFinder(email, emailProvider, password):
    # linking provider to imap
    addressDictonary = {
        "gmail": "imap.gmail.com",
        "outlook": "imap-mail.outlook.com",
        "office365": "outlook.office365.com",
        "yahoo": "imap.mail.yahoo.co.uk",
        "verizon": "incoming.verizon.net",
    }

    imap_url = addressDictonary[str(emailProvider)]

    def get_body(msg):
        if msg.is_multipart():
            return get_body(msg.get_payload(0))

        else:
            return msg.get_payload(None, True)

    def search(key, value, imap):
        results, data = imap.search(None, key, '"{}'.format(value))
        return data

    def get_emails(result_btyes):
        megs = []
        for nums in result_btyes[0].split():
            typ, data = imap.fetch(num, "(RFC822)")
            msgs.append(data)
        return msgs

    # create an IMAP4 class with SSL
    imap = imaplib.IMAP4_SSL(imap_url)

    # authenticate
    imap.login(email, password)

    imap.select("INBOX")

    result, data = imap.fetch(b"10", "(RFC822)")
    raw = email.message_from_bytes(data[0][1])
    print(get_body(raw))

    msgs = get_emails(search("FROM", "no-reply@mail.tesco.com", imap))

    for msg in msgs:
        print(get_body(email.message_from_bytes(msg[])))

    
    # close the connection and logout
    imap.close()
    imap.logout()
