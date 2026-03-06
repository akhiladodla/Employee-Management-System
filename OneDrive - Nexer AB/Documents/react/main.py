from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, eid: int, name: str, salary: float):
        self.__id = eid
        self.__name = name
        self.__salary = salary

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @abstractmethod
    def calculateBonus(self) -> float:
        """Calculate bonus for the employee. Must be overridden."""
        pass


class Payable(ABC):
    @abstractmethod
    def processSalary(self):
        """Handle salary processing for the employee."""
        pass


class FullTimeEmployee(Employee, Payable):
    def calculateBonus(self) -> float:
        return self.salary * 0.10

    def processSalary(self):
        print(f"Processing salary for full-time employee {self.name}: {self.salary}")


class PartTimeEmployee(Employee, Payable):
    def calculateBonus(self) -> float:
        return self.salary * 0.05

    def processSalary(self):
        print(f"Processing salary for part-time employee {self.name}: {self.salary}")


def main():
    employees = [
        FullTimeEmployee(1, "Alice", 60000),
        PartTimeEmployee(2, "Bob", 30000),
        FullTimeEmployee(3, "Charlie", 80000),
    ]

    for emp in employees:
        print(f"ID: {emp.id}, Name: {emp.name}, Salary: {emp.salary}")
        print(f"Bonus: {emp.calculateBonus()}")
        emp.processSalary()
        print("-" * 30)


if __name__ == "__main__":
    main()
 