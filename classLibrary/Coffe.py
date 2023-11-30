from classLibrary.BaseModel import BaseModel
from peewee import *
class Coffe(BaseModel):
    id = PrimaryKeyField(column_name="id", unique=True)
    type = CharField(column_name="type",max_length=100)
    size = CharField(column_name="size",max_length=2)
    price = FloatField(column_name = "price",null=False)

    class Meta:
        table_name = "coffe"


    def getName(self):
        return self._name

    def getSize(self):
        return self._size

    def getPrice(self):
        return self._price