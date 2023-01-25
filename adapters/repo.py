from classic.components.component import component
from classic.sql_storage.repository import BaseRepository
from sqlalchemy import select, desc, text, func, delete

from adapters.tables import employees, departments
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

    def get(self, reference):
        return self.session.query(self.model).filter_by(id=reference).one_or_none()

    def get_list(self, limit: int = None, offset: int = None):
        limit = limit or 5
        offset = offset or 0
        query = select(self.model)
        return self.session.execute(query).scalars().all()[offset: offset + limit]

    def delete(self, reference):
        #query = delete(self.model).where(self.model.id==reference).exdelete(synchronize_session='fetch')
        #q1 = select(self.model).filter_by(id=1)
        q = self.session.query(self.model).filter(self.model.id==reference).delete()
        self.session.commit()
        return q

    def filer_by(self, params):
        entity_model = self.session.query(self.model).filter_by(**params).one_or_none()
        return entity_model


@component
class EmployeeRepository(SQLiteRepository, BaseRepository):
    model = Employee

    def get_departments_performance_sum(self):
        query_text_join = text("select department.name as department, sum(performance)"
                               " from employee  join department on employee.department_id=department.id"
                               " group by department.name")
        query = select(
            departments.c.name,
            func.sum(employees.c.performance)
        ).select_from(employees.join(departments)).group_by(departments.c.name)
        return self.session.execute(query).all()

    def get_most_successfully_employees(self):
        query = (select(self.model).order_by(desc(self.model.performance))
                 .limit(1))
        return self.session.execute(query).scalar()

    def proba_relationsships_alchemy(self):
        """Изучал relatioships  как можно доставать обьекты через relationship"""
        from aplications.dataclases import Department, Employee
        query = select(Employee).order_by(desc(Employee.id)).limit(1)
        department = self.session.execute(query).scalar()
        print('!!!!!!!', department.departmen.name)
