from abc import ABC, abstractmethod


class Department:
    codes = {
        'managers': 1,
        'sellers': 2,
    }

    def __init__(self, name: str, code: int):
        self.name = name
        self.code = code

    @classmethod
    def getDepartmentByName(cls, name: str) -> 'Department':
        return Department(name, cls.codes[name])


class Employee(ABC):
    DAILY_WORK_HOURS = 8

    def __init__(self, code: int, name: str, salary: float, dpt_name: str):
        self.code = code
        self.name = name
        self.salary = salary
        self.__department = Department.getDepartmentByName(dpt_name)

    @abstractmethod
    def calc_bonus(self) -> float:
        pass

    @classmethod
    def get_hours(cls) -> int:
        """Returns the employee's daily work hours"""
        return cls.DAILY_WORK_HOURS

    def get_department(self) -> str:
        """Returns the department's name"""
        return self.__department.name

    def set_department(self, dpt_name: str) -> None:
        self.__department.name = dpt_name


class Manager(Employee):
    DEFAULT_DEPARTMENT_NAME = 'managers'
    PERCENT_BONUS = 15

    def __init__(self, code: int, name: str, salary: float):
        super().__init__(code, name, salary, self.DEFAULT_DEPARTMENT_NAME)

    def calc_bonus(self) -> float:
        return self.salary * (self.PERCENT_BONUS / 100)


class Seller(Employee):
    DEFAULT_DEPARTMENT_NAME = 'sellers'
    PERCENT_BONUS = 15

    def __init__(self, code: int, name: str, salary: float):
        super().__init__(code, name, salary, self.DEFAULT_DEPARTMENT_NAME)
        self.__sales = 0

    def calc_bonus(self) -> float:
        return self.__sales * (self.PERCENT_BONUS / 100)

    def get_sales(self) -> float:
        return self.__sales

    def put_sales(self, sales: float) -> float:
        self.__sales += sales
