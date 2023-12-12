from classLibrary import Manager,Smena,User,Pay,Coffe,Additional
from  dto import ManagerDto,CoffeDto,AdditionalDto,PayDto,SmenaDto,UserDto

def LoginManager(login,password):
    valManager = ManagerDto.GetManagerByLoginAndPassword(login,password)
    if valManager == login and valManager.password == password:
        return valManager
    else:
        return None

_mainMenu:str
_buyMenu = ""
_smenaMenu:str

while True:
    password = input("Введите пароль от кассы")
    if password == "qwerty":
        login = input("Введите логин")
        passwordManager = input("Введите пароль")
        manager = LoginManager(login,passwordManager)
        if manager is None:
            break
        _mainMenu = f"{manager.name()}\n1 - Открыть смену"
        choice = input(_mainMenu)
        if choice == "1":
            smena = SmenaDto.CreateSmena(manager)
            payList = []
            while True:
                _mainMenu = f"{manager.name()}\n1 - Закрыть смену\n2 - Покупка"
                choice = input(_mainMenu)
                if choice == "2":
                    while True:
                        coffes = CoffeDto.GetAllCoffe()
                        _buyMenu = ""
                        for coffe in coffes:
                            _buyMenu += f"{coffe.id} {coffe.name} {coffe.price}\n"
                        _buyMenu += "6-выход"
                        choice = input(_buyMenu)
                        if choice !="6":
                            coffe = CoffeDto.GetCoffeByID(int(choice))
                            _buyMenu = ""
                            additionals = AdditionalDto.GetAllAdditional()
                            for additional in additionals:
                                _buyMenu+= f"{additional.id} {additional.size} {additional.type}\n"
                            _buyMenu += "6-выход"
                            choice = input(_buyMenu)
                            if choice !="6":
                                additional = AdditionalDto.GetAllAdditionalById(int(choice))
                            else:
                                pass
                        elif choice == "6":
                            break
                        else:
                            continue
                        phone = input("введите номер телеона пользователя")
                        user = UserDto.ChangeUserByPhone(phone)
                        pay = Pay.Pay(eMoney=True,
                                      client=User,
                                      additionals=additional,
                                      coffes=coffe)
                        payList.append(pay)

                elif choice == "1":
                    summ = 0
                    for payItem in payList:
                        summ+=payItem.coffe.price()
                        if not payItem.additionals is None:
                            summ+=payItem.additionals.price()

                    smena.sum(summ)
                    SmenaDto.CloseSmena(smena,summ)
                    break

        break
    else:
        continue
