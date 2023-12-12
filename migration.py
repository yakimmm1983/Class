from classLibrary.User import User
from classLibrary.Additional import Additional
from classLibrary.Pay import Pay
from classLibrary.Coffe import Coffe
from classLibrary.Manager import Manager
from classLibrary.Smena import Smena


if __name__ == "__main__":
    status = "ok"
    try:
        Smena.drop_table()
        Pay.drop_table()
        User.drop_table()
        Additional.drop_table()
        Coffe.drop_table()
        Manager.drop_table()

    except Exception as e:
        status = f"Drop error {e}"
    # try:
    #     User.create_table()
    #     Additional.create_table()
    #     Coffe.create_table()
    #     Pay.create_table()
    #     Manager.create_table()
    #     Smena.create_table()
    #
    # except Exception as e:
    #     status = f"Create error {e}"
    print(f"Migration {status}")