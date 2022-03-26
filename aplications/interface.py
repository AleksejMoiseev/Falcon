import abc
from aplications.dataclases import BaseModel
from classic.components.component import component


@component
class RepositoryInterface(metaclass=abc.ABCMeta):
    model: BaseModel

    @abc.abstractmethod
    def add(self, entity):
        raise NotImplementedError


class DepartmentServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_department(self, params):
        pass


class EmployeeServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_employee(self, params):
        pass

    @abc.abstractmethod
    def get_departments_performance_sum(self):
        pass

    @abc.abstractmethod
    def get_most_successfully_employees(self):
        pass