from notification_service import NotificationService
from email_service import EmailService
from sms_service import SMSService

sms=SMSService()
ns=NotificationService(sms)
ns.Notify("Hello")