
class Notification:
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print("Email sent:", message)



class SMSNotification(Notification):
    def send(self, message):
        print("SMS sent:", message)




n1 = EmailNotification()
n2 = SMSNotification()

n1.send("Hello User!")
n2.send("Welcome!")
