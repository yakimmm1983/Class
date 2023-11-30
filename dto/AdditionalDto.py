from classLibrary.Additional import Additional

def GetAllAdditional():
    additionals = Additional.select().dicts()
    returnAdditionals = []
    for additional in additionals:
        returnAdditionals.append(Additional(id = Additional["id"],type = Additional["type"],size = Additional["size"],price = Additional["price"]))
    return returnAdditionals
def GetAdditionalById(Id:int):
    additional = Additional.select().where(Additional.id == Id).get()
    return additional