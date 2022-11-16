import win32com.client as win32
from task import Task, Network
from data_manipulation import Email

# !TODO NEED TO VERIFY INTERNET IN FLOW
class Mail:
    def __init__(self, recipient: str, subject: str, body: str):
        self.recipient = recipient
        self.first_name = Email(recipient).extract_first_name()
        self.subject = subject
        self.body = body
        self.send = None
    
    def __str__(self):
        return f"Mail object containing; recipient: {self.recipient}, \n\
                first_name: {self.first_name}, subject: {self.subject}, \n\
                body: {self.body}, and send status: {self.send}"

    def __repr__(self):
        pass

    def verify_internet(self):
        return Network().is_connected
    
    def send(self) -> None:
        task = Task()
        task.request_loop()

    def old_send_task(self, response: str) -> bool:
        """function to verify information prior to email"""
        approve = ["yes", "y"]
        return response.lower() in approve

    def verify_data(self) -> None:
        task_loop = True
        failed_attempts = 0
        while task_loop:
            print("Verify the information:\n")
            print(f"\trecipient:\n\t\t {self.recipient},\n\n \tsubject:\n\t\t {self.subject},\n\n \tbody:\n\t\t {self.body(self.recipient)}\n")
            ask = input("Verify information for email:")
            if step := self.send_task(ask):
                self.send_mail(self.recipient, self.subject, self.body(self.recipient))
            else:
                print("Aborting...")
                task_loop = False

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

