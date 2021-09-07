def calculate_salary(employees_list):
    my_count = 0
    for i in employees_list:
        my_count += i[1]
    return my_count
