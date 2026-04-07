# class User:
#     def __init__(self, username):
#         self.username = username

#     def login(self):
#             print(f"{self.username} logged in")
# class Admin(User):
#     def delete(self):
#         print("Admin can delete the user")

# a = Admin("abc")
# a.delete()        
class notifucation:
    def send(self):
    
        print("Notofication send")

class emailnotifucation(notifucation):
    def send(self):
        print("emil send")

class SMMSNotification(notifucation):
    def send(self):
        print("SMS notification send")

q = emailnotifucation()
q.send()


class Animal:
    def sound(self):
        print("this animal maing sound loudly")
class Dog(Animal):
    def sound(self):
        print("the dog barks")

animal = Animal()
animal.sound()
dog = Dog()
dog.sound()

class BankAccount:
    def __init__(self, acc_no, balance):
        self._acc_no = acc_no
        self.__balnce = balance

    def check_balance (self):
        print(self._balnce)

    def deposit(self, amount):
        self.__balnce += amount


    def withdrw(self, amount):
        if self.__balnce<amount:
            print("Insufficient fund")
            return
        self.__balnce -= amount
        print(f"withdraw success fu;ly -Balnce:{self.__balnce}")

pabva = BankAccount(acc_no=1234, balance = 500)
# pabva.check_balance()
pabva.deposit(100)
pabva.withdrw(50)