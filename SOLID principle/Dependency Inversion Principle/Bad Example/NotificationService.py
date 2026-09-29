from Email import Email
from SMS import SMS

class NotificationService:

    '''
    Notification Service is a High Level module
    which is depended on low level module like Email,SMS
    Probles:
        1)Tight Copuling
        2)Not Flexible
        3)Might face issue while Testing
    '''
    def __init__(self):
        self.email_service=Email()
        self.sms_service=SMS()

    def sendByEmail(self,message):
        self.email_service.sendEmail(message)

    def sendBySMS(self,message):
        self.sms_service.sendSMS(message)

nn=NotificationService()
nn.sendByEmail("Email responses is ok")
nn.sendBySMS("Sms is working great")