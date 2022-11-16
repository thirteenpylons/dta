from ..mailer_with_task import *
from ..lib.key_data import email as EMAIL
body = """
hello

"""
email = EMAIL[0]
first_name = "Christian"
subject = "..."
body = "..."
mail = Mail(email, subject, body)

def test_mail_str_():
    printed_mail = print(mail)
    assert printed_mail == f"Mail object containing; recipient: {email}, \n\
                first_name: {first_name}, subject: {subject}, \n\
                body: {body}, and send status: None"

def test_mail_repr_():
    pass

def test_mail_recipient():
    assert mail.recipient == email

def test_mail_first_name():
    assert mail.first_name == first_name

def test_mail_subject():
    assert mail.subject == "Thank you Christian!"

def test_mail_body():
    assert mail.body == body

def test_mail_verify_internet():
    assert mail.verify_internet() == True

def test_Body():
    pass


class TestMail:

    email = EMAIL[0]
    subject = "..."
    body = "..."

    mail_object = Mail(email, subject, body)

    def send_task(self, response: str) -> bool:
        """function to verify information prior to email"""
        approve = ["yes", "y"]
        if response.lower() in approve:
            return True
        else:
            return False

    def verify_data(self) -> None:
        task_loop = True
        failed_attempts = 0
        while task_loop:
            print("Verify the information:\n")
            print(f"\trecipient:\n\t\t {recipient},\n\n \tsubject:\n\t\t {subject},\n\n \tbody:\n\t\t {body(recipient)}\n")
            ask = input("Verify information for email:")
            step = send_task(ask)
            if not step:
                print("Aborting...")
                task_loop = False
            else:
                send_mail(recipient, subject, body(recipient))

    def send_mail(self, recipient: str, subject: str, body: str) -> None:
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)

        mail.To = recipient
        mail.Subject = subject
        mail.HTMLBody = f"<body>{body}</body>"

        mail.Send()
        print(f"Email sent to {recipient} successfully!")


class Subject:
    def __init__(self):
        pass


class Body:
    def __init__(self, name=None):
        self.name = name

    def loopback(self):
        pass

