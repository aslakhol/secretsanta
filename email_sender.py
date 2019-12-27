import smtplib
import ssl


class EmailSender:
    port = 465
    password = "HmdNsr%75*&u"
    sender_email = "testlak.utvikler@gmail.com"
    receiver_email = "testlak.utvikler@gmail.com"

    def send(self, receiver_email, message):
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=context) as server:
            server.login("testlak.utvikler@gmail.com", self.password)
            # Send email here
            server.sendmail(self.sender_email, receiver_email, message)
