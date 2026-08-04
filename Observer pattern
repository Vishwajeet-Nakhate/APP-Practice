from abc import ABC, abstractmethod


# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


# Concrete Observers
class EmailSubscriber(Observer):
    def update(self, message):
        print(f"Email received: {message}")


class SMSSubscriber(Observer):
    def update(self, message):
        print(f"SMS received: {message}")


# Subject
class YouTubeChannel:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, observer):
        self._subscribers.append(observer)

    def unsubscribe(self, observer):
        self._subscribers.remove(observer)

    def notify(self, message):
        for subscriber in self._subscribers:
            subscriber.update(message)

    def upload_video(self, title):
        print(f"\nNew video uploaded: {title}")
        self.notify(f"New video available: {title}")


# Client Code
if __name__ == "__main__":
    channel = YouTubeChannel()

    email = EmailSubscriber()
    sms = SMSSubscriber()

    channel.subscribe(email)
    channel.subscribe(sms)

    channel.upload_video("Observer Pattern in Python")

    channel.unsubscribe(sms)

    channel.upload_video("Factory Pattern Explained")
