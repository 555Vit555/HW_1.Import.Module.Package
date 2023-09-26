from datetime import datetime

from application.salary import calculate_salary

from application.db.people import get_employees

if __name__ == '__main__':



    print(datetime.today())

    calculate_salary(100500)
    get_employees('Иванов Иван Иванович')





