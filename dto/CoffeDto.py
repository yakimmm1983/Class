from classLibrary.Coffe import Coffe


def GetAllCoffe():
    coffes = Coffe.select().dicts()
    returnCoffe = []
    for coffe in coffes:
        returnCoffe.append(Coffe(id = coffe["id"],type = coffe["type"],size = coffe["size"],price = coffe["price"]))
    return returnCoffe
def GetCoffeById(Id:int):
    coffe = Coffe.select().where(Coffe.id == Id).get()
    return coffe