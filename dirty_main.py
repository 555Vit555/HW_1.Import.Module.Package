from datetime import datetime

from application.salary import *

from application.db.people import *



if __name__ == '__main__':



    print(datetime.today())

    calculate_salary(100500)
    get_employees('Иванов Иван Иванович')