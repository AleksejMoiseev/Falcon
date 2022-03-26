from classic.components.component import component
from classic.sql_storage.repository import BaseRepository
from sqlalchemy import select, desc

from aplications.dataclases import Chat, Employee
from aplications.interface import RepositoryInterface


@component
class Proba(BaseRepository):

    def add(self, chat: Chat):
        self.session.add(chat)
        self.session.flush()


@component
class SQLiteRepository(BaseRepository, RepositoryInterface):

    def add(self, entity):
        entity_model = self.session.query(self.model).filter_by(id=entity.id).one_or_none()
        if entity_model:
            return entity_model
        self.session.add(entity)
        self.session.flush()
        return entity


@component
class EmployeeRepository(SQLiteRepository, BaseRepository):
    model = Employee

    def get_departments_performance_sum(self):
        pass

    def get_most_successfully_employees(self):
        query = (select(self.model).order_by(desc(self.model.performance))
                 .limit(1))
        return self.session.execute(query).scalar()
