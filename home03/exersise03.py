import datetime


MINIMAL_YEAR = 2005


class Employee:
    def __init__(self, first_name='', last_name='', job_title='', year_of_registration=0):
        if not first_name:
            raise ValueError('First name is required!')
        if not last_name:
            raise ValueError('Last name is required!')
        if not job_title:
            raise ValueError('Job Title is required!')

        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title

        if not year_of_registration:
            year_of_registration = datetime.date.today().year

        self.year_of_registration = year_of_registration

    def __str__(self):
        return 'Employee: {first_name!s}, {last_name!s}, {job_title!s}, ' \
               '{year_of_registration!s}'.format_map(self.__dict__)

    @staticmethod
    def read_employee():
        first_name = input('Please enter First name: ')
        last_name = input('Please enter Last name: ')
        job_title = input('Please enter Job title: ')
        hired_date = read_year('Please enter Hired date (or leave blank for current year): ')

        return Employee(first_name, last_name, job_title, hired_date)


def check_valid_year(year):
    return MINIMAL_YEAR <= year <= datetime.date.today().year


def safe_input(description, my_function=None):
    while True:
        try:
            input_value = int(input(description))
            if my_function and not my_function(input_value):
                raise ValueError('Incorrect value')
        except ValueError as error:
            print('Error: ', error)
        else:
            return input_value


def read_year(message):
    return safe_input(message, check_valid_year)


def main():
    number_of_people = safe_input('How many people do you want to add: ')
    employees = []

    while len(employees) < number_of_people:
        try:
            employee = Employee.read_employee()
        except ValueError as error:
            print('Error: ', error)
        else:
            employees.append(employee)
        finally:
            print()

    year = read_year('Please enter year of registration: ')

    for person in employees:
        if person.year_of_registration >= year:
            print(person)


if __name__ == '__main__':
    main()