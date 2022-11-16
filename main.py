"""
Map out usage for Mail
Mail:
    ...

use:
    recipient = "first.last@email.com"
    first_name = Email(recipient).extract_first_name()
    subject = "Email subject"
    body = Body(first_name).interview()
    mail = Mail(recipient)
    mail.verify_internet() # need to implicitly verify internet
    mail.send()


    TODO TAKE DATA OUT OF TASK:
        send data locally from Mail()
            -> use task for verification

"""
