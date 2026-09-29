from abc import ABC, abstractmethod

class NotificationChannel:

    @abstractmethod
    def send(self,message):
        pass
    