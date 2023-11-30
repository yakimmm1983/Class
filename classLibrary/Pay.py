import datetime
from classLibrary.User import User
from classLibrary.Coffe import Coffe
from classLibrary.Additional import Additional
from classLibrary.BaseModel import BaseModel
from peewee import *
class Pay(BaseModel):
    id = PrimaryKeyField(column_name="id",unique=True)
    date = DateField(column_name="date")
    eMoney = BooleanField(column_name="e_money")
    client = ForeignKeyField(User,related_name = "pay_user_client_id",to_field="id")
    sum = FloatField(column_name="sum")
    additionals = ForeignKeyField(Additional,related_name="pay_additional_additional_id",to_field="id")
    class Meta:
        table_name = "pay"
    # _date: datetime.date
    # _eMoney: bool
    # _client: User
    # _sum = 0.0
    # _coffes: list[Coffe]
    # _additionals: list[Additional]
    # def __init__(self, eMoney, client, coffes=None, additionals=None):
    #     if additionals is None:
    #         additionals = []
    #     if coffes is None:
    #         coffes = []
    #     self._eMoney = eMoney
    #     self._client = client
    #     self._coffes = coffes
    #     self._date = datetime.datetime.now().date()
    #     self._additionals = additionals
    #     if len(coffes) !=0:
    #         for coffe in coffes:
    #             self._sum += coffe.getPrice()
    #     if len(additionals) !=0:
    #         for additional in additionals:
    #             self._sum += additional.getPrice()
    # def getSum(self):
    #     return self._sum


