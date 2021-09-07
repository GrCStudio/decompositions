from db import peoples
from application import salary
from datetime import datetime


if __name__ == '__main__':
    print(datetime.now())
    print(salary.calculate_salary(peoples.employees_list))
