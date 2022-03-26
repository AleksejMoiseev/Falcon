from classic.components.component import component
from sqlalchemy import select

from aplications.dataclases import Department, Employee
from aplications.interface import (
    RepositoryInterface, DepartmentServiceInterface,
    EmployeeServiceInterface
)
from classic.app.dto import DTO


class DepartmentDTO(DTO):
    pk: int = None
    name: str


class EmployeeDTO(DTO):
    pk: int = None
    full_name: str
    performance: float
    department_id: int


@component
class ServiceDepartment(DepartmentServiceInterface):
    repo_employee: RepositoryInterface

    def create_department(self, params):
        dto = DepartmentDTO(**params)
        data = dto.dict()
        department = Department(**data)
        return self.repo_employee.add(department)


@component
class ServiceEmployee(EmployeeServiceInterface):
    employee_repositories: RepositoryInterface

    def create_employee(self, params):
        dto = EmployeeDTO(**params)
        data = dto.dict()
        employee = Employee(**data)
        return self.employee_repositories.add(employee)

    def get_departments_performance_sum(self):
        pass

    def get_most_successfully_employees(self):
        return self.employee_repositories.get_most_successfully_employees()


if __name__ == '__main__':
    d = DepartmentDTO(pk=1, name='Al')
    print(d.dict())