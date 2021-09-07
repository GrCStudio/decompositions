from db.peoples import *
from application.salary import *
from datetime import *


if __name__ == '__main__':
    print(datetime.now())
    print(calculate_salary(employees_list))