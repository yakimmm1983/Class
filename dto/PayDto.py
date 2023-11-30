from classLibrary.User import User
from classLibrary.Pay import Pay
from classLibrary.Additional import Additional
from classLibrary.Coffe import Coffe
import datetime
def CreatePay(user:User,additional:Additional,coffe:Coffe):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    summ = additional.price + coffe.price
    user.bonus += summ*0.1
    pay = Pay(date=date,additionals=additional,client=user,eMoney=False,sum=summ)
    pay.save()
    user.save()
    return pay
