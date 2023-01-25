from sqlalchemy import (
    MetaData, Table, Column, Integer, String, Float, ForeignKey, VARCHAR
)
from sqlalchemy.orm import registry, relationship

from aplications.dataclases import Chat, Department, Employee

mapper_registry = registry()
metadata = MetaData()

chats = Table(
    'chats', metadata,
    Column('pk', Integer, primary_key=True),
    Column('order_date', VARCHAR(128)),
)

departments = Table(
    'department', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', VARCHAR(30)),
)

employees = Table(
    'employee', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('full_name', VARCHAR(30)),
    Column('performance', Float),
    Column('department_id', Integer, ForeignKey('department.id')),
)

mapper_registry.map_imperatively(Chat, chats)
mapper_registry.map_imperatively(Department, departments, properties={
    'employee': relationship(Employee, backref='department', uselist=False)
})
mapper_registry.map_imperatively(Employee, employees, properties={
    'departmen': relationship(Department)
})