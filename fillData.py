from classLibrary.Additional import Additional
from classLibrary.Coffe import Coffe
from classLibrary.Manager import Manager
def CreateAdditional():
    additional = Additional(size = "XL",type = "Сироп",price = 30.0)
    additional.save()
    additional1 = Additional(size="L", type="Сироп", price=20.0)
    additional1.save()
    additional2 = Additional(size="M", type="Сироп", price=10.0)
    additional2.save()
def CreateCoffe():
    coffe = Coffe(type = "Лате",size = "M",price = 120)
    coffe.save()
    coffe1 = Coffe(type = "Капучино",size = "M",price = 130)
    coffe1.save()
    coffe2 = Coffe(type = "Раф",size = "M",price = 140)
    coffe2.save()
def CreateManager():
    manager = Manager(login = "123",password = "123",name = "Олег",phone = "89561242356",bonus = 0)
    manager.save()
if __name__=="__main__":
    CreateAdditional()
    CreateCoffe()
    CreateManager()
