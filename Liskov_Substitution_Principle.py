from abc import ABC, abstractmethod


class Contact:
    def __init__(self, name, phone, email, msg):
        self.name = name
        self.phone = phone
        self.email = email
        self.msg = msg

    def __str__(self):
        return self.name


class notification(ABC):
    @abstractmethod
    def notify(self, message, para):
        pass


class email_Notify(notification):
    def notify(self, message, para):
        print(f"you are{message} and {para}")


class Phon_Notify(notification):
    def notify(self, message, para):
        print(f"you messages here {message} and  {para}")


con = Contact("sumilon", "0193846746", "sumi@gmail.com", "god boy")
email=email_Notify()
email.notify(con.msg,con.email)
phn=Phon_Notify()
phn.notify(con.msg,con.phone)