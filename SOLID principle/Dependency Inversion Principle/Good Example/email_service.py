from NotificationChannel import NotificationChannel

class EmailService(NotificationChannel):

    def send(self,message):
        print(f"Email Sending: {message}")