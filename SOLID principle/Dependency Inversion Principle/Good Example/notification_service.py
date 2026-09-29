from NotificationChannel import NotificationChannel

class NotificationService:
    def __init__(self,channel:NotificationChannel):
        self.channel=channel

    def Notify(self,message):
        self.channel.send(message)
