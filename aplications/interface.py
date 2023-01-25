import abc
from aplications.dataclases import BaseModel
from classic.components.component import component


@component
class RepositoryInterface(metaclass=abc.ABCMeta):
    model: BaseModel

    @abc.abstractmethod
    def add(self, entity):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference):
        raise NotImplementedError

    @abc.abstractmethod
    def get_list(self, limit: int = None, offset: int = None):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, reference):
        raise NotImplementedError


class DepartmentServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_department(self, params):
        pass

    @abc.abstractmethod
    def get_lists(self):
        pass

    @abc.abstractmethod
    def get(self, pk):
        pass

    @abc.abstractmethod
    def delete(self, reference):
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

    @abc.abstractmethod
    def get_new_relations_ships(self):
        ...