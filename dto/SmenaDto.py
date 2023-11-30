from classLibrary.Smena import Smena
from classLibrary.Manager import Manager
import datetime
def CreateSmena(manager:Manager):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    timeOpen = datetime.datetime.now().strftime("%H:%M:%S")
    smena = Smena(data = date,timeOpen=timeOpen,manager = manager)
    smena.save()
def CloseSmena(smena:Smena,summ:float):
    smena.timeClose = datetime.datetime.now().strftime("%H:%M:%S")
    smena.sum = summ
    smena.save()